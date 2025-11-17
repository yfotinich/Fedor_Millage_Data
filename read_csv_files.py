import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
import psycopg2

# Load environment variables from .env file
load_dotenv()

# Set path for reading the CSV files
csv_path = os.getenv("CSV_PATH", "../Millage_Data/")

# Set variables for PostgreSQL connection
# Database connection parameters
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Validate required environment variables
required_vars = ["DB_HOST", "DB_NAME", "DB_USER", "DB_PASSWORD"]
missing_vars = [var for var in required_vars if not os.getenv(var)]
if missing_vars:
    raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")

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
