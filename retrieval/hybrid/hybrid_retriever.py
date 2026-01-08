class HybridRetriever:
    def __init__(self, weaviate_search):
        self.search_engine = weaviate_search

    def retrieve(self, query: str):
        return self.search_engine.search(query)
