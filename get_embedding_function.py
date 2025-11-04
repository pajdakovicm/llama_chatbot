# from langchain_community.embeddings.ollama import OllamaEmbeddings
# from langchain_community.embeddings.bedrock import BedrockEmbeddings


# def get_embedding_function():
#     embeddings = BedrockEmbeddings(
#         credentials_profile_name="default", region_name="us-east-1"
#     )
#     # embeddings = OllamaEmbeddings(model="nomic-embed-text")
#     return embeddings

# from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain_ollama import OllamaEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings


def get_embedding_function():
    # Option 1: Use Ollama (local, no API keys needed)
    # embeddings = OllamaEmbeddings(model="llama3.2")
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return embeddings

    # Option 2: Use Hugging Face (local, no API keys)
    # embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    # return embeddings
