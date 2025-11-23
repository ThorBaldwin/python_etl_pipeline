"""
Data Loading Module

This module contains the Loader class for saving cleaned data
to CSV and ZIP formats.
"""

import zipfile
import os


class Loader:
    """Handles saving and compressing cleaned data."""

    def save_to_csv(self, df, output_path):
        """
        Save DataFrame to a CSV file.

        Creates the output directory if it doesn't exist.

        Args:
            df (pandas.DataFrame): The cleaned data to save
            output_path (str): File path where CSV should be saved
        """
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df.to_csv(output_path, index=False)
        print(f"Saved cleaned data to {output_path}")

    def zip_output(self, file_path):
        """
        Compress a CSV file into a ZIP archive.

        The ZIP file is created in the same directory with the same name
        but with a .zip extension instead of .csv.

        Args:
            file_path (str): Path to the CSV file to compress
        """
        zip_path = file_path.replace(".csv", ".zip")
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
            z.write(file_path, os.path.basename(file_path))
        print(f"Created ZIP file: {zip_path}")
