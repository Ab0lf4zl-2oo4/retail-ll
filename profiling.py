import psycopg2
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
from pathlib import Path

calendar=pd.read_csv('dataset/calendar.csv')
customers=pd.read_csv('dataset/customers.csv')
inventory=pd.read_csv('dataset/inventory.csv')
products=pd.read_csv('dataset/products.csv')
sales=pd.read_csv('dataset/sales.csv')
stores=pd.read_csv('dataset/stores.csv')
print('calander')
print(calendar.columns)
print('customers')
print(customers.columns)
print('inventory')
print(inventory.columns)
print('products')
print(products.columns)
print('sales')
print(sales.columns)
print('stores')
print(stores.columns)


print(sales['sales_id'].is_unique)
print(stores['store_id'].is_unique)
print(products['product_id'].is_unique)
print(customers['customer_id'].is_unique)
print(calendar['date'].is_unique)

print('s')
print(sales['customer_id'].isin(customers['customer_id']).all())
print(sales['store_id'].isin(stores['store_id']).all())
print(sales['product_id'].isin(products['product_id']).all())
print(sales['date'].isin(calendar['date']).all())
print(inventory['product_id'].isin(products['product_id']).all())
print(inventory['store_id'].isin(stores['store_id']).all())

x=sales.merge(calendar,on='date',how='inner',indicator=True)
print(x)

print(products['category'].nunique)

import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus
from pathlib import Path

connection_string = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=DESKTOP-JKUS70M;"
    "DATABASE=retail;"
    "Trusted_Connection=yes;"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)

engine = create_engine(
    "mssql+pyodbc:///?odbc_connect="
    + quote_plus(connection_string)
)

data_folder = Path(r"C:\Users\Pascal\Desktop\nyc\dataset")

for file in data_folder.glob("*.csv"):
    df = pd.read_csv(file)

    table_name = file.stem.lower()

    df.to_sql(
        name=table_name,
        con=engine,
        if_exists="fail",
        index=False
    )

print("انتقال فایل‌ها تمام شد.")