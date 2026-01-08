class EnterpriseRAGEngine:
    def __init__(self, retrieval_pipeline, llm):
        self.retrieval = retrieval_pipeline
        self.llm = llm

    def answer(self, question: str):
        documents = self.retrieval.run(question)

        context = "\n\n".join(
            f"[Source: {d.metadata.get('source', 'N/A')}] {d.page_content}"
            for d in documents
        )

        response = self.llm.generate(
            question=question,
            context=context
        )

        return response
