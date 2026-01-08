def enterprise_schema():
    return {
        "class": "EnterpriseDoc",
        "vectorizer": "none",
        "properties": [
            {"name": "text", "dataType": ["text"]},
            {"name": "file_name", "dataType": ["text"]},
            {"name": "chunk_type", "dataType": ["text"]},
            {"name": "parent_id", "dataType": ["int"]},
            {"name": "created_time", "dataType": ["text"]},
            {"name": "department", "dataType": ["text"]}
        ]
    }
