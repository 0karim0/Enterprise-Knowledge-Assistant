import json
import os
from chunkers.semantic_chunker import SemanticChunker
from chunkers.hierarchical_chunker import HierarchicalChunker
from embeddings.embedding_factory import get_embedding_model
from vectorstore.weaviate_client import get_weaviate_client
from vectorstore.indexer import WeaviateIndexer
from embeddings.embedding_config import EMBEDDING_MODEL

STAGING_DIR = "data/staging"

def run_pipeline():
    embedding = get_embedding_model(EMBEDDING_MODEL)
    client = get_weaviate_client()
    indexer = WeaviateIndexer(client, embedding)

    chunker = HierarchicalChunker()

    for file in os.listdir(STAGING_DIR):
        with open(os.path.join(STAGING_DIR, file), "r") as f:
            document = json.load(f)

        chunks = chunker.chunk(document)
        indexer.index(chunks)

if __name__ == "__main__":
    run_pipeline()
