E-Commerce Data Warehouse & BI Platform

An end-to-end Business Intelligence project built with Python, SQL Server, Power BI, and Apache Airflow. The project covers initial data profiling, data preparation, dimensional data warehouse design, automated data quality checks, controlled data loading, workflow orchestration, and management reporting.

Project Overview

The goal of this project was to build a structured and repeatable data pipeline that transforms raw retail data into a reliable data warehouse and turns it into actionable business insights through Power BI dashboards.

The project was developed in stages, from understanding the source data to implementing automated warehouse loading and delivering a management-focused BI solution.

Technology Stack

Python: Initial data inspection, profiling, and data transfer to SQL Server.

SQL Server: Staging, dimensional data warehouse, stored procedures, data quality checks, and audit logging.

Apache Airflow: DAG-based workflow orchestration and task dependency management.

Power BI: Data modeling, DAX measures, interactive dashboards, and management reporting.

Project Workflow

1. Initial Data Profiling and Ingestion

Inspected and profiled the source data to understand its structure and quality.

Used Python for initial data preparation and transfer to SQL Server.

Loaded the source data into staging tables to establish a foundation for downstream processing.

2. Staging Layer and Data Warehouse Design

Created a dedicated stg schema to organize and inspect incoming data.

Reviewed source data and prepared it for warehouse loading.

Designed a separate dw schema using dimensional modeling principles.

Organized analytical data into dimension and fact tables to support reporting and business analysis.

3. Automated Data Quality and Audit Logging

Developed a stored procedure, dbo.usp_DataQualityChecks, to validate data quality.

Implemented checks for referential integrity, invalid values, missing relationships, and business-rule violations.

Created an audit schema and tables to store data quality reports and validation results.

4. Controlled and Repeatable Data Warehouse Loading

Developed dbo.usp_Load_DataWarehouse to automate loading data into warehouse tables.

Implemented duplicate prevention using conditional insert logic.

Used TRY/CATCH and transaction handling to improve error handling and loading reliability.

Addressed identity-column handling and database permissions required by the loading process.

Designed the loading process to support repeatable execution without inserting duplicate records.

5. Workflow Orchestration with Apache Airflow

Apache Airflow was introduced as a learning and orchestration component, even though SQL Server Agent could have been sufficient for this project's scheduling requirements.

Installed Airflow in a local WSL2 Ubuntu environment.

Configured connectivity between Airflow and SQL Server.

Created a DAG named ecommerce_dw_pipeline with four dependent tasks:

check_connection — verifies database connectivity.

check_data_quality — runs data quality validation.

load_data_warehouse — executes the warehouse loading procedure.

validate_warehouse — validates the resulting warehouse data.

Executed the pipeline and resolved database permission issues encountered during integration.

Used task dependencies to ensure that later stages run in the intended order.

6. Power BI Dashboard and Management Reporting

Built a Power BI dashboard to support business analysis and management decision-making.

The BI layer focuses on turning warehouse data into interactive reports and analytical views. Depending on the available data and implemented report pages, these can include:

Sales and revenue analysis.

Customer spending and segmentation.

Product and category performance.

Order and payment status analysis.

Inventory monitoring.

Interactive filtering and context-aware measures using DAX.

Architecture
Source Data | v Python: Initial Profiling and Ingestion | v SQL Server: Staging Schema (stg) | v Data Quality Checks + Audit Logging | v Dimensional Data Warehouse (dw) | v Power BI: Interactive Dashboards 

Orchestration layer: Apache Airflow coordinates the database checks, warehouse loading, and post-load validation through a four-task DAG.

Key Engineering Concepts

Staging and dimensional data warehouse architecture.

Fact and dimension table design.

SQL stored procedures for repeatable processing.

Data quality validation and audit logging.

Duplicate prevention and controlled loading.

Transaction handling and exception management.

Identity-column handling and database permission management.

Airflow DAGs, task dependencies, and SQL Server integration.

Power BI data modeling, DAX, and interactive reporting.

Repository Structure

ecommerce-data-warehouse-bi/ ├── sql/ │ ├── schema_and_table_creation.sql │ ├── load_staging.sql │ ├── load_datawarehouse.sql │ ├── data_quality_checks.sql │ └── validation_queries.sql ├── airflow/ │ └── dags/ │ └── bi_project_first.py ├── powerbi/ │ ├── dashboard.pbix │ └── screenshots/ ├── docs/ │ └── architecture.png ├── .gitignore └── README.md 

The repository structure may differ slightly from this example.

Setup and Execution

Create the required SQL Server schemas and tables using the provided SQL scripts.

Load the source data into the staging layer.

Configure the required database connection in Apache Airflow.

Review the database permissions required by the stored procedures.

Run the ecommerce_dw_pipeline DAG.

Connect Power BI to the warehouse and open the report.

Connection details, passwords, and environment-specific settings must be configured locally and should not be committed to the repository.

Project Scope and Learning Outcomes

This project combines data preparation, SQL development, warehouse design, data quality engineering, workflow orchestration, and business intelligence reporting in one practical workflow.

It also provided hands-on experience with SQL Server security and permissions, repeatable ETL execution, pipeline debugging, and integration between Windows-hosted SQL Server and Airflow running in WSL2.

Future Improvements

Add automated tests for stored procedures and data quality rules.

Improve audit logging with pipeline run identifiers, timestamps, and failure details.

Implement incremental loading based on a reliable change-tracking strategy.

Add Airflow retries, failure notifications, and operational monitoring.

Document the dimensional model and dashboard metrics in greater detail.

Tools: Python · SQL Server · SQL · Apache Airflow · Power BI · DAX

Project focus: Data Warehousing · ETL · Data Quality · Workflow Orchestration · Business Intelligence
