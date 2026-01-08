from langchain.retrievers.document_compressors import EmbeddingsRedundantFilter
from langchain_openai import OpenAIEmbeddings

class RedundancyFilter:
    def __init__(self):
        self.filter = EmbeddingsRedundantFilter(
            embeddings=OpenAIEmbeddings()
        )

    def apply(self, documents):
        return self.filter.compress_documents(documents)
