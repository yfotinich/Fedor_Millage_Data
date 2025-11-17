import pandas as pd
import os

from sqlalchemy import create_engine
import psycopg2

# # Reading the CSV files
# # Georgia Millage Rates CSV file path
# file_name = "GA_MILLAGE_RATES.csv"
csv_path = "../Millage_Data/"
# file_path = os.path.join(csv_path, file_name)

# df_ga = pd.read_csv(file_path)

# print("Data loaded successfully!")
# print(f"Shape: {df_ga.shape}")
# print("\nFirst few rows:")
# print(df_ga.head())#(1643, 9)

# # Ohio Millage Rates CSV file path
# file_name = "OH_MILLAGE_RATES.csv"
# csv_path = "../Millage_Data/"
# file_path = os.path.join(csv_path, file_name)

# df_oh = pd.read_csv(file_path)
# print("Data loaded successfully!")
# print(f"Shape: {df_oh.shape}")
# print("\nFirst few rows:")
# print(df_oh.head())#(4473, 16)

# # Ohio Millage Rates CSV file path
# file_name = "TX_MILLAGE_RATES.csv"
# csv_path = "../Millage_Data/"
# file_path = os.path.join(csv_path, file_name)

# df_tx = pd.read_csv(file_path)
# print("Data loaded successfully!")
# print(f"Shape: {df_tx.shape}")# (5575, 10)
# print("\nFirst few rows:")
# print(df_tx.head())




# Database connection parameters
DB_HOST = "157.245.7.53"
DB_NAME = "rivka"
DB_USER = "postgres"
DB_PASSWORD = "4pZK_bx_TV"

# Method 1: Using SQLAlchemy (Recommended - easier for pandas)
# Create connection string
connection_string = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"

# Create engine
engine = create_engine(connection_string)

# # Write dataframe to PostgreSQL
# try:
#     # Write to table
#     df_tx.to_sql(
#         'eugene_test_texas_millage',      # Table name
#         engine,                  # Database engine
#         if_exists='replace',     # Options: 'fail', 'replace', 'append'
#         index=False,             # Don't write dataframe index as column
#         chunksize=2000           # Write in chunks for large datasets
#     )
#     print("Data written successfully!")
    
# except Exception as e:
#     print(f"Error writing to database: {e}")

# # Write dataframe to PostgreSQL
# try:
#     # Write to table
#     df_ga.to_sql(
#         'eugene_test_georgia_millage',      # Table name
#         engine,                  # Database engine
#         if_exists='replace',     # Options: 'fail', 'replace', 'append'
#         index=False,             # Don't write dataframe index as column
#         chunksize=2000           # Write in chunks for large datasets
#     )
#     print("Data written successfully!")
    
# except Exception as e:
#     print(f"Error writing to database: {e}")

# # Write dataframe to PostgreSQL  
# try:
#     # Write to table
#     df_oh.to_sql(
#         'eugene_test_ohio_millage',      # Table name
#         engine,                  # Database engine
#         if_exists='replace',     # Options: 'fail', 'replace', 'append'
#         index=False,             # Don't write dataframe index as column
#         chunksize=2000           # Write in chunks for large datasets
#     )
#     print("Data written successfully!")
    
# except Exception as e:
#     print(f"Error writing to database: {e}")
    
    
files_list = ["TX_MILLAGE_RATES.csv", "GA_MILLAGE_RATES.csv", "OH_MILLAGE_RATES.csv"]


for file in files_list:
    file_path = os.path.join(csv_path, file)
    df = pd.read_csv(file_path)
    state_code = file.split("_")[0]  # Extract state code from filename
    table_name = f"millage_rates_{state_code.upper()}"
    
    try:
        df.to_sql(
            table_name,
            engine,
            if_exists='replace',
            index=False,
            chunksize=2000
        )
        print(f"Data for {state_code} written successfully!")
        
    except Exception as e:
        print(f"Error writing data for {state_code} to database: {e}")