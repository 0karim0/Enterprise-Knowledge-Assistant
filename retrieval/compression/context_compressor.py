from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain_openai import ChatOpenAI

class ContextCompressor:
    def __init__(self):
        self.llm = ChatOpenAI(temperature=0)
        self.compressor = LLMChainExtractor.from_llm(self.llm)

    def compress(self, query, documents):
        return self.compressor.compress_documents(documents, query)
