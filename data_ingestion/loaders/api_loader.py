import requests
from ..parsers.metadata_extractor import extract_metadata

class APILoader:
    """
    Pull data from enterprise APIs and structure it
    """
    def __init__(self, endpoint: str, headers: dict = None, params: dict = None):
        self.endpoint = endpoint
        self.headers = headers or {}
        self.params = params or {}

    def load(self):
        response = requests.get(self.endpoint, headers=self.headers, params=self.params)
        if response.status_code != 200:
            raise Exception(f"API request failed with {response.status_code}")
        
        data = response.json()
        # Optional: flatten nested structures if needed
        metadata = {"source": self.endpoint}
        return {
            "text": str(data),
            "metadata": metadata
        }
