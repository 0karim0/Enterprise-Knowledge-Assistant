import os
from bs4 import BeautifulSoup
from ..parsers.metadata_extractor import extract_metadata

class HTMLLoader:
    """
    Load HTML files and extract clean text
    """
    def __init__(self, file_path: str):
        self.file_path = file_path
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"HTML file {file_path} not found")

    def load(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')
            # Remove scripts/styles
            for script in soup(["script", "style"]):
                script.decompose()
            text = soup.get_text(separator="\n")
        metadata = extract_metadata(self.file_path)
        return {
            "text": text,
            "metadata": metadata
        }
