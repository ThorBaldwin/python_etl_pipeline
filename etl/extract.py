"""
Data Extraction Module

This module contains the Extractor class for retrieving data from
the NYC Open Data API.
"""

import requests
import os


class Extractor:
    """Extracts JSON data from NYC Open Data API."""

    def __init__(self, api_url, app_token=None):
        """
        Initialize the Extractor with API credentials.

        Args:
            api_url (str): The NYC Open Data API endpoint URL
            app_token (str, optional): Authentication token for API access.
                If not provided, will check SOCRATA_APP_TOKEN environment variable.
        """
        self.api_url = api_url
        self.app_token = app_token or os.getenv("SOCRATA_APP_TOKEN")

    def extract_data(self, limit=100):
        """
        Fetch records from the NYC DOB API.

        Args:
            limit (int): Maximum number of records to retrieve. Default is 100.

        Returns:
            list: JSON data containing job application records

        Raises:
            Exception: If the API request fails or returns an error status code
        """
        print(f"Extracting data from API: {self.api_url}")
        params = {"$limit": limit}
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36"
        }

        if self.app_token:
            headers["X-App-Token"] = self.app_token
            params["$$app_token"] = self.app_token

        response = requests.get(self.api_url, params=params, headers=headers)

        if response.status_code == 200:
            data = response.json()
            print(f"Extracted {len(data)} records.")
            return data
        else:
            error_msg = f"API request failed: {response.status_code}"
            try:
                error_detail = response.text[:200]
                error_msg += f"\nError details: {error_detail}"
            except Exception:
                pass
            raise Exception(error_msg)
