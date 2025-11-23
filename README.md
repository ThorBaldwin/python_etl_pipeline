# NYC DOB Job Application Filings ETL Pipeline

This project extracts, transforms, and loads (ETL) data from the NYC Department of Buildings (DOB) Job Application Filings dataset.

## Project Structure
```
python_etl_pipeline/
├── etl/
│   ├── __init__.py
│   ├── extract.py      # Data extraction from NYC Open Data API
│   ├── transform.py    # Data cleaning and transformation
│   └── load.py         # Data loading (CSV and ZIP)
├── data/
│   └── processed/      # Output directory for cleaned data
├── main.py             # Main ETL pipeline script
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Setup Instructions

### 1. Clone the Repository
```bash
git clone 
cd python_etl_pipeline
```

### 2. Create Virtual Environment

**On macOS/Linux:**
```bash
python3 -m venv venv
```

**On Windows:**
```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**On macOS/Linux:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

## Running the ETL Pipeline

With the virtual environment activated, run:
```bash
python main.py
```

The pipeline will:
1. Extract data from the NYC DOB API
2. Clean and transform the data
3. Save the output to `data/processed/dob_filings_clean.csv`
4. Create a compressed ZIP file `data/processed/dob_filings_clean.zip`

## Code Quality Check

### Generate flake8 HTML Report

Install flake8 and flake8-html:
```bash
pip install flake8 flake8-html
```

Generate the HTML report:
```bash
flake8 --format=html --htmldir=flake8-report --max-line-length=88 --exclude=venv
```

The report will be generated in the `flake8-report/` directory. Open `flake8-report/index.html` in your browser to view it.

## Requirements

- Python 3.7+
- See `requirements.txt` for Python package dependencies

## Data Source

NYC Department of Buildings Job Application Filings:
https://data.cityofnewyork.us/Housing-Development/DOB-Job-Application-Filings/ic3t-wcy2

## Author

Thor Baldwin

## License

This project is for educational purposes.