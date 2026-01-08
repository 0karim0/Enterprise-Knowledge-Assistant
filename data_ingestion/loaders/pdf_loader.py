import os
from typing import List, Dict
from PyPDF2 import PdfReader
from ..parsers.metadata_extractor import extract_metadata

class PDFLoader:
    """
    Load PDF files and return structured documents with metadata
    """
    def __init__(self, file_path: str):
        self.file_path = file_path
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"PDF file {file_path} not found")

    def load(self) -> Dict:
        reader = PdfReader(self.file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        
        metadata = extract_metadata(self.file_path)
        return {
            "text": text,
            "metadata": metadata
        }

# Example usage:
# loader = PDFLoader("data/docs/sample.pdf")
# doc = loader.load()
# print(doc["metadata"])
