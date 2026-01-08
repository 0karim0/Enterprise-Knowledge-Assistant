import os
import datetime

def extract_metadata(file_path: str) -> dict:
    """
    Extract basic metadata from file
    """
    stats = os.stat(file_path)
    return {
        "file_name": os.path.basename(file_path),
        "created_time": datetime.datetime.fromtimestamp(stats.st_ctime).isoformat(),
        "modified_time": datetime.datetime.fromtimestamp(stats.st_mtime).isoformat(),
        "size_bytes": stats.st_size
    }
