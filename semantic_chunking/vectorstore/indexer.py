from langchain.vectorstores import Weaviate
from langchain.docstore.document import Document

class WeaviateIndexer:
    def __init__(self, client, embedding):
        self.store = Weaviate(
            client=client,
            index_name="EnterpriseDoc",
            text_key="text",
            embedding=embedding
        )

    def index(self, chunks):
        docs = [
            Document(
                page_content=chunk["text"],
                metadata=chunk["metadata"]
            )
            for chunk in chunks
        ]
        self.store.add_documents(docs)
