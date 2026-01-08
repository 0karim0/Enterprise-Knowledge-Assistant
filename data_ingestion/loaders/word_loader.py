import os
from docx import Document as DocxDocument
from ..parsers.metadata_extractor import extract_metadata

class WordLoader:
    """
    Load Word (.docx) files and return structured documents with metadata
    """
    def __init__(self, file_path: str):
        self.file_path = file_path
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Word file {file_path} not found")

    def load(self):
        doc = DocxDocument(self.file_path)
        text = "\n".join([p.text for p in doc.paragraphs])
        metadata = extract_metadata(self.file_path)
        return {
            "text": text,
            "metadata": metadata
        }