from datetime import datetime

from airflow.sdk import dag, task
from airflow.providers.microsoft.mssql.hooks.mssql import MsSqlHook


CONNECTION_ID = "sqlserver"


@dag(
    dag_id="ecommerce_dw_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["ecommerce", "data-warehouse", "sql-server"],
)
def ecommerce_dw_pipeline():

    @task
    def check_connection():
        """Verify the SQL Server connection."""
        hook = MsSqlHook(mssql_conn_id=CONNECTION_ID)
        conn = hook.get_conn()

        try:
            cursor = conn.cursor()
            cursor.execute("SELECT DB_NAME(), SUSER_SNAME()")
            result = cursor.fetchone()

            print(f"Database: {result[0]}")
            print(f"Login: {result[1]}")

            if result[0].lower() != "retail":
                raise ValueError(
                    f"Expected database 'retail', got '{result[0]}'"
                )
        finally:
            conn.close()

    @task
    def check_data_quality():
        """Run the existing data quality stored procedure."""
        hook = MsSqlHook(mssql_conn_id=CONNECTION_ID)

        hook.run(
            "EXEC dbo.usp_DataQualityChecks;",
            autocommit=True,
        )

        print("Data quality procedure executed.")

    @task
    def load_data_warehouse():
        """Execute the actual data warehouse loading procedure."""
        hook = MsSqlHook(mssql_conn_id=CONNECTION_ID)

        hook.run(
            "EXEC dbo.usp_Load_DataWarehouse;",
            autocommit=True,
        )

        print("Data warehouse loading procedure executed successfully.")

    @task
    def validate_warehouse():
        """Validate row counts in the warehouse tables."""
        hook = MsSqlHook(mssql_conn_id=CONNECTION_ID)

        tables = [
            "dw.dimcustomers",
            "dw.dimproducts",
            "dw.dimstores",
            "dw.factsales",
            "dw.factinventory",
        ]

        conn = hook.get_conn()

        try:
            cursor = conn.cursor()

            for table in tables:
                cursor.execute(
                    f"SELECT COUNT_BIG(*) FROM {table}"
                )
                count = cursor.fetchone()[0]
                print(f"{table}: {count} rows")
        finally:
            conn.close()

        print("Warehouse validation completed.")

    connection = check_connection()
    quality = check_data_quality()
    load = load_data_warehouse()
    validation = validate_warehouse()

    connection >> quality >> load >> validation


ecommerce_dw_pipeline()
