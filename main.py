"""
NYC DOB ETL Pipeline - Main Execution Script

This script orchestrates the Extract, Transform, Load (ETL) pipeline for
NYC Department of Buildings Job Application Filings data.

The pipeline performs three main steps:
1. Extract: Retrieves data from NYC Open Data API
2. Transform: Cleans and standardizes the data
3. Load: Saves data to CSV and ZIP formats

Usage:
    python main.py

Output:
    - data/processed/dob_filings_clean.csv
    - data/processed/dob_filings_clean.zip

Author: Thor Baldwin
Date: November 2025
"""

from etl.extract import Extractor
from etl.transform import Transformer
from etl.load import Loader


def main():
    """
    Execute the complete ETL pipeline.

    This function coordinates the three ETL steps:
    - Extracts data from NYC Open Data API
    - Transforms and cleans the raw data
    - Loads the cleaned data to CSV and ZIP files

    Raises:
        Exception: If any step of the pipeline fails
    """
    print("Starting ETL pipeline...")

    api_url = "https://data.cityofnewyork.us/resource/ic3t-wcy2.json"
    output_path = "data/processed/dob_filings_clean.csv"

    try:
        # Extract
        extractor = Extractor(api_url)
        raw_data = extractor.extract_data()

        # Transform
        transformer = Transformer()
        transformed_data = transformer.clean_data(raw_data)

        # Load
        loader = Loader()
        loader.save_to_csv(transformed_data, output_path)
        loader.zip_output(output_path)

        print("ETL pipeline complete.")

    except Exception as e:
        print(f"Pipeline failed: {e}")
        raise


if __name__ == "__main__":
    main()
