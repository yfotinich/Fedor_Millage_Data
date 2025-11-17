# Product Context

## Why This Project Exists
This project automates the process of loading millage rate data from CSV files into a centralized PostgreSQL database. Millage rates are property tax rates used by local governments, and maintaining historical data across multiple states is crucial for analysis and reporting.

## Problems It Solves
1. **Manual Data Loading**: Eliminates the need to manually import CSV data into the database
2. **Data Organization**: Maintains separate tables per state for clear data segmentation
3. **Scalability**: Can easily be extended to support additional states by adding CSV files to the list
4. **Error Handling**: Provides feedback when data loading fails, helping identify issues quickly

## How It Should Work
1. User places CSV files in the `../Millage_Data/` directory
2. Script reads each CSV file (TX_MILLAGE_RATES.csv, GA_MILLAGE_RATES.csv, OH_MILLAGE_RATES.csv)
3. For each file:
   - Extract state code from filename
   - Load CSV data into pandas DataFrame
   - Write data to corresponding PostgreSQL table (e.g., `millage_rates_TX`)
   - Replace existing data if table already exists
4. Report success or errors for each state's data load

## User Experience Goals
- **Simple Execution**: Run a single Python script to load all data
- **Clear Feedback**: See confirmation messages for successful loads and detailed error messages if issues occur
- **Easy Setup**: New developers can configure credentials via .env file and start immediately
- **Secure**: Database credentials never exposed in the codebase or version control

## Key Features
- Batch processing of multiple CSV files
- Automatic table naming based on state codes
- Chunked data insertion (2000 rows at a time) for efficient memory usage
- Replace strategy for tables (fresh data each run)
