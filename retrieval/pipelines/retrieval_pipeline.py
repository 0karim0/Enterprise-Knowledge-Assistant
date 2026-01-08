class RetrievalPipeline:
    def __init__(
        self,
        query_rewriter,
        retriever,
        reranker,
        redundancy_filter,
        compressor
    ):
        self.query_rewriter = query_rewriter
        self.retriever = retriever
        self.reranker = reranker
        self.redundancy_filter = redundancy_filter
        self.compressor = compressor

    def run(self, user_query):
        rewritten_query = self.query_rewriter.rewrite(user_query)

        docs = self.retriever.retrieve(rewritten_query)

        reranked_docs = self.reranker.run(rewritten_query, docs)

        filtered_docs = self.redundancy_filter.apply(reranked_docs)

        compressed_docs = self.compressor.compress(
            rewritten_query, filtered_docs
        )

        return compressed_docs
