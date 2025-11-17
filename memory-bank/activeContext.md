# Active Context

## Current Work Focus
Securing the repository by:
1. Extracting hardcoded database credentials from `read_csv_files.py`
2. Moving credentials to `.env` file
3. Updating script to load credentials from environment variables
4. Setting up `.gitignore` to prevent credential leaks
5. Creating `.env.template` for sharing setup instructions

## Recent Changes
- Created comprehensive memory-bank documentation structure
- Documented project purpose, architecture, and technical stack
- Identified security issue: hardcoded database credentials in source code

## Next Steps
1. Create `.env` file with extracted credentials
2. Update `read_csv_files.py` to use `python-dotenv` and `os.getenv()`
3. Create `.gitignore` to exclude `.env` and other sensitive files
4. Create `.env.template` with placeholder values for team sharing

## Active Decisions and Considerations

### Security Priority
- **Critical**: Database credentials currently exposed in source code
- **Risk**: Credentials visible in GitHub repository (public or private)
- **Solution**: Move to environment variables immediately

### Environment Variable Naming
Using clear, descriptive names:
- `DB_HOST` - Database server address
- `DB_NAME` - Database name
- `DB_USER` - Database username
- `DB_PASSWORD` - Database password
- `CSV_PATH` - Path to CSV directory (optional, has default)

### Script Refactoring Approach
- Add `from dotenv import load_dotenv` import
- Add `load_dotenv()` call at script start
- Replace hardcoded values with `os.getenv()` calls
- Add validation to ensure required variables are set

## Important Patterns and Preferences

### Code Organization
- Keep imports at the top
- Load environment variables before using them
- Maintain existing error handling structure
- Keep success/error messages clear

### Documentation
- Memory-bank follows hierarchical structure (.clinerules pattern)
- All credential references should point to environment variables
- Template files should include helpful comments

## Learnings and Project Insights

### Current State
- Single Python script handles entire ETL process
- Three states currently supported (TX, GA, OH)
- Remote PostgreSQL database hosted at [REDACTED_DB_HOST]
- CSV files stored in parent directory (`../Millage_Data/`)

### Git Repository
- Repository: https://github.com/yfotinich/Fedor_Millage_Data.git
- Latest commit: 9861b5644f88b29a8d0d9bcc27ecb6f35f0595aa
- **Security concern**: Credentials may already be in git history

### Future Considerations
- May need to rotate database credentials if already pushed to git
- Consider adding requirements.txt for dependency management
- Could expand to support additional states
- Might benefit from incremental updates vs. full replacement
