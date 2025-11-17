# System Patterns

## Architecture Overview
Simple ETL (Extract, Transform, Load) pipeline with a linear execution flow:
```
CSV Files → Pandas DataFrame → SQLAlchemy → PostgreSQL Database
```

## Key Components

### 1. Data Source Layer
- **Location**: `../Millage_Data/` directory (relative to script)
- **Format**: CSV files with naming pattern `{STATE_CODE}_MILLAGE_RATES.csv`
- **States**: TX, GA, OH

### 2. Data Processing Layer
- **Library**: Pandas
- **Function**: `pd.read_csv()` loads CSV into DataFrame
- **Processing**: Minimal transformation, primarily data transport

### 3. Database Connection Layer
- **Library**: SQLAlchemy + psycopg2
- **Connection Pattern**: Connection string format
  ```
  postgresql://{user}:{password}@{host}:5432/{database}
  ```
- **Engine**: SQLAlchemy engine created once, reused for all operations

### 4. Data Loading Layer
- **Method**: `DataFrame.to_sql()`
- **Strategy**: `if_exists='replace'` - overwrites existing tables
- **Performance**: `chunksize=2000` for memory-efficient bulk inserts
- **Indexing**: `index=False` - doesn't write DataFrame index to database

## Design Patterns

### File Naming Convention
Files follow pattern: `{STATE_CODE}_MILLAGE_RATES.csv`
- Script extracts state code using: `file.split("_")[0]`
- Table name generated as: `millage_rates_{STATE_CODE}`

### Loop-Based Processing
Single loop processes all files sequentially:
```python
for file in files_list:
    # Extract state code
    # Load data
    # Write to database
    # Handle errors
```

### Error Handling
Try-catch block per file ensures one file's failure doesn't stop others:
```python
try:
    # Database write operation
    print(success_message)
except Exception as e:
    print(error_message)
```

## Critical Implementation Paths

### Configuration to Execution Flow
1. Set CSV path and database credentials
2. Create SQLAlchemy engine
3. Iterate through file list
4. Per file: read → transform table name → write to DB

### Credential Management Pattern (After Refactoring)
1. Load credentials from environment variables using `os.getenv()`
2. Use `python-dotenv` to load from .env file
3. Validate required credentials exist before connection attempt

## Database Schema Pattern
- Table per state: `millage_rates_TX`, `millage_rates_GA`, `millage_rates_OH`
- Schema inferred from CSV columns (pandas auto-creates from DataFrame)
- Full table replacement on each run (no incremental updates)
