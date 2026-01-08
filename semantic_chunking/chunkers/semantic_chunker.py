from langchain.text_splitter import RecursiveCharacterTextSplitter
from .base_chunker import BaseChunker

class SemanticChunker(BaseChunker):
    def __init__(
        self,
        chunk_size: int = 800,
        chunk_overlap: int = 150
    ):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=["\n\n", "\n", ".", " ", ""]
        )

    def chunk(self, document):
        chunks = self.splitter.split_text(document["text"])
        metadata = document["metadata"]

        return [
            {
                "text": chunk,
                "metadata": {
                    **metadata,
                    "chunk_type": "semantic"
                }
            }
            for chunk in chunks
        ]
