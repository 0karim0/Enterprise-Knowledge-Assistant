import re

def clean_text(text: str) -> str:
    """
    Clean and normalize text
    """
    # Remove multiple newlines
    text = re.sub(r'\n+', '\n', text)
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)
    # Strip
    return text.strip()
