import weaviate

def get_weaviate_client():
    return weaviate.Client(
        url="http://localhost:8080"
    )
