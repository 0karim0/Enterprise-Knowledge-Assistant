from langchain.embeddings.openai import OpenAIEmbeddings

def get_embedding_model(model_name: str):
    if model_name == "openai":
        return OpenAIEmbeddings()
    else:
        raise ValueError("Unsupported embedding model")
