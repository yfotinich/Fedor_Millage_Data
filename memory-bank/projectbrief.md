# Project Brief

## Project Name
Fedor Millage Data

## Project Overview
A Python-based data pipeline that reads millage rate data from CSV files for multiple US states (Texas, Georgia, Ohio) and loads them into a PostgreSQL database.

## Core Requirements
1. Read CSV files containing millage rate data for TX, GA, and OH states
2. Connect to a PostgreSQL database securely
3. Load data into state-specific tables in the database
4. Handle errors gracefully during data loading
5. Secure credential management using environment variables

## Primary Goals
- Automate the process of loading millage rate data from CSV files to PostgreSQL
- Maintain separate tables per state for organized data storage
- Ensure database credentials are not exposed in version control
- Provide a clean, reproducible setup for other developers

## Project Scope
- Data source: CSV files located in `../Millage_Data/` directory
- Target states: TX (Texas), GA (Georgia), OH (Ohio)
- Database: PostgreSQL hosted remotely
- Technology: Python with pandas and SQLAlchemy for data processing and database operations

## Success Criteria
- All CSV files successfully loaded into PostgreSQL tables
- Credentials secured in environment variables
- Code is shareable and reproducible via .env.template
- Repository properly configured with .gitignore to prevent credential leaks
