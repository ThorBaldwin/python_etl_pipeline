"""
Data Transformation Module

This module contains the Transformer class for cleaning and
standardizing NYC DOB filing data.
"""

import pandas as pd


class Transformer:
    """Cleans and transforms DOB filing data."""

    def clean_data(self, data):
        """
        Convert JSON to DataFrame and perform data cleaning operations.

        Cleaning steps performed:
        1. Convert JSON list to pandas DataFrame
        2. Filter to keep only relevant columns (14 fields)
        3. Remove rows with missing job numbers
        4. Remove duplicate records based on job number
        5. Standardize column names to lowercase

        Args:
            data (list): Raw JSON data from the API

        Returns:
            pandas.DataFrame: Cleaned and transformed data ready for analysis
        """
        print("Transforming data...")
        df = pd.DataFrame(data)

        keep_cols = [
            "job__",
            "job_type",
            "borough",
            "house__",
            "street_name",
            "block",
            "lot",
            "community_board",
            "applicant_s_first_name",
            "applicant_s_last_name",
            "filing_status",
            "job_status_descrp",
            "initial_cost",
            "total_est_fee",
        ]
        df = df[[c for c in keep_cols if c in df.columns]]
        df = df.dropna(subset=["job__"])
        df = df.drop_duplicates(subset=["job__"])
        df.columns = [c.lower().strip() for c in df.columns]

        print(f"Transformed dataset has {len(df)} rows and {len(df.columns)} columns.")
        return df
