import os

def list_files(directory: str, extensions: list):
    """
    Recursively list files with specific extensions
    """
    result = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if any(file.lower().endswith(ext) for ext in extensions):
                result.append(os.path.join(root, file))
    return result
