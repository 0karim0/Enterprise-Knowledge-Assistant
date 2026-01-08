from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI

class QueryRewriter:
    def __init__(self, model_name="gpt-4o-mini"):
        self.llm = ChatOpenAI(model=model_name, temperature=0)

        self.prompt = PromptTemplate(
            input_variables=["query"],
            template = """
You are an enterprise-grade information retrieval assistant.

Your task is to rewrite the user's query into a clear, precise, and technically accurate search query
optimized for semantic and hybrid document retrieval systems (vector search + keyword search).

Guidelines:
- Preserve the original user intent.
- Remove ambiguity, filler words, and conversational phrasing.
- Expand implicit technical meaning where appropriate.
- Use domain-specific terminology when applicable.
- Do NOT answer the query.
- Do NOT add new information.
- Output only the rewritten query.

Original User Query:
{query}

Rewritten Search Query:
"""

)

        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)

    def rewrite(self, query: str) -> str:
        return self.chain.run(query).strip()
