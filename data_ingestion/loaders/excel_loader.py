import os
import pandas as pd
from ..parsers.metadata_extractor import extract_metadata

class ExcelLoader:
    """
    Load Excel files and convert each sheet to structured text
    """
    def __init__(self, file_path: str):
        self.file_path = file_path
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Excel file {file_path} not found")

    def load(self):
        xls = pd.ExcelFile(self.file_path)
        sheets_text = {}
        for sheet_name in xls.sheet_names:
            df = pd.read_excel(self.file_path, sheet_name=sheet_name)
            # Convert table to string
            sheets_text[sheet_name] = df.to_csv(index=False)
        
        metadata = extract_metadata(self.file_path)
        return {
            "text": sheets_text,
            "metadata": metadata
        }
