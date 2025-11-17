import pandas as pd
import os

from sqlalchemy import create_engine
import psycopg2

# Set path for reading the CSV files
csv_path = "../Millage_Data/"


# Set variables for PostgreSQL connection
# Database connection parameters
DB_HOST = "157.245.7.53"
DB_NAME = "rivka"
DB_USER = "postgres"
DB_PASSWORD = "4pZK_bx_TV"

# Using SQLAlchemy (easier for pandas)
# Create connection string
connection_string = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"

# Create engine
engine = create_engine(connection_string)

    

# List of CSV files to read    
files_list = ["TX_MILLAGE_RATES.csv", "GA_MILLAGE_RATES.csv", "OH_MILLAGE_RATES.csv"]

# Loop through each file, read it into a DataFrame, and write to PostgreSQL
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