# Technical Context

## Technologies Used

### Programming Language
- **Python 3.x** - Primary language for the ETL script

### Core Dependencies
1. **pandas** - Data manipulation and CSV reading
   - Used for: Reading CSV files, DataFrame operations
   
2. **SQLAlchemy** - SQL toolkit and ORM
   - Used for: Database engine creation, connection management
   - Provides: High-level database abstraction
   
3. **psycopg2** - PostgreSQL adapter for Python
   - Used for: Low-level PostgreSQL connectivity
   - Required by SQLAlchemy for PostgreSQL connections

4. **python-dotenv** (to be added)
   - Used for: Loading environment variables from .env file
   - Purpose: Secure credential management

## Development Setup

### Environment Variables Required
```
DB_HOST - PostgreSQL server IP address
DB_NAME - Database name
DB_USER - Database username
DB_PASSWORD - Database password
CSV_PATH - Path to directory containing CSV files (optional, has default)
```

### Installation Steps
1. Install Python 3.x
2. Install dependencies:
   ```bash
   pip install pandas sqlalchemy psycopg2-binary python-dotenv
   ```
3. Create `.env` file with database credentials (see .env.template)
4. Ensure CSV files are in `../Millage_Data/` directory
5. Run script: `python read_csv_files.py`

## Technical Constraints

### Data Source
- CSV files must be located at `../Millage_Data/` relative to script
- File naming must follow pattern: `{STATE_CODE}_MILLAGE_RATES.csv`
- CSV files must be readable by pandas (valid CSV format)

### Database
- PostgreSQL database must be accessible (network connectivity required)
- Database must exist before running script
- User must have CREATE TABLE and INSERT permissions
- Port 5432 (PostgreSQL default) must be accessible

### Performance
- Chunk size set to 2000 rows for bulk inserts
- All data loaded into memory before database write
- Sequential processing (one file at a time)

## File Structure
```
Fedor_Millage_Data/
├── .clinerules
├── .env                    # Credentials (git-ignored)
├── .env.template          # Template for sharing
├── .gitignore            # Git ignore patterns
├── read_csv_files.py     # Main ETL script
├── memory-bank/          # Documentation
│   ├── projectbrief.md
│   ├── productContext.md
│   ├── systemPatterns.md
│   ├── techContext.md
│   ├── activeContext.md
│   └── progress.md
└── ../Millage_Data/      # CSV files (external directory)
    ├── TX_MILLAGE_RATES.csv
    ├── GA_MILLAGE_RATES.csv
    └── OH_MILLAGE_RATES.csv
```

## Tool Usage Patterns

### Running the Script
```bash
python read_csv_files.py
```

### Expected Output
```
Data for TX written successfully!
Data for GA written successfully!
Data for OH written successfully!
```

### Error Output Example
```
Error writing data for TX to database: <error details>
```

## Security Considerations
- Database credentials stored in .env file (not committed to git)
- .env file must be created locally by each developer
- .env.template provides structure without sensitive data
- Connection uses standard PostgreSQL authentication
