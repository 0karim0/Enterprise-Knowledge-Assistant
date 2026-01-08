from langchain.text_splitter import RecursiveCharacterTextSplitter
from .base_chunker import BaseChunker

class HierarchicalChunker(BaseChunker):
    def __init__(self):
        self.parent_splitter = RecursiveCharacterTextSplitter(
            chunk_size=2000,
            chunk_overlap=200
        )
        self.child_splitter = RecursiveCharacterTextSplitter(
            chunk_size=400,
            chunk_overlap=100
        )

    def chunk(self, document):
        parent_chunks = self.parent_splitter.split_text(document["text"])
        results = []

        for parent_id, parent in enumerate(parent_chunks):
            child_chunks = self.child_splitter.split_text(parent)
            for child in child_chunks:
                results.append({
                    "text": child,
                    "metadata": {
                        **document["metadata"],
                        "parent_id": parent_id,
                        "chunk_type": "hierarchical"
                    }
                })
        return results
