class RerankPipeline:
    def __init__(self, reranker):
        self.reranker = reranker

    def run(self, query, docs):
        return self.reranker.rerank(query, docs)
