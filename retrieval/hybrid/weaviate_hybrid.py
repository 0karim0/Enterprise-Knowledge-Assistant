from langchain_weaviate import WeaviateVectorStore

class WeaviateHybridSearch:
    def __init__(self, client, index_name):
        self.vectorstore = WeaviateVectorStore(
            client=client,
            index_name=index_name,
            text_key="text"
        )

    def search(self, query: str, k: int = 20):
        return self.vectorstore.similarity_search(
            query,
            k=k,
            hybrid=True,
            alpha=0.5  # balance BM25 vs vector
        )
