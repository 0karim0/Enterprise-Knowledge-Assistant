import os
from loaders.pdf_loader import PDFLoader
from loaders.word_loader import WordLoader
from loaders.excel_loader import ExcelLoader
from loaders.html_loader import HTMLLoader
from utils.file_utils import list_files
from utils.logging_utils import setup_logger
from utils import config
from parsers.text_parser import clean_text
import json

logger = setup_logger("ingestion_pipeline", config.LOG_FILE)

LOADER_MAPPING = {
    "pdf": PDFLoader,
    "word": WordLoader,
    "excel": ExcelLoader,
    "html": HTMLLoader
}

def ingest_data():
    all_files = []
    for ext_list in config.SUPPORTED_EXTENSIONS.values():
        all_files.extend(list_files(config.DATA_DIR, ext_list))

    logger.info(f"Found {len(all_files)} files to ingest")

    for file_path in all_files:
        ext = os.path.splitext(file_path)[1].lower()
        loader_class = None
        for key, exts in config.SUPPORTED_EXTENSIONS.items():
            if ext in exts:
                loader_class = LOADER_MAPPING[key]
                break
        if loader_class is None:
            logger.warning(f"Skipping unsupported file {file_path}")
            continue

        try:
            loader = loader_class(file_path)
            doc = loader.load()
            doc["text"] = clean_text(doc["text"] if isinstance(doc["text"], str) else str(doc["text"]))
            
            # Save to staging
            os.makedirs(config.STAGING_DIR, exist_ok=True)
            staging_path = os.path.join(config.STAGING_DIR, doc["metadata"]["file_name"] + ".json")
            with open(staging_path, "w", encoding="utf-8") as f:
                json.dump(doc, f, ensure_ascii=False, indent=4)
            logger.info(f"Ingested and saved: {file_path}")
        except Exception as e:
            logger.error(f"Failed to process {file_path}: {e}")

if __name__ == "__main__":
    ingest_data()
