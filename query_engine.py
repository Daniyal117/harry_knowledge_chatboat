import logging
import sys
import os
from llama_index.core import VectorStoreIndex
from llama_index.core.settings import Settings  # ✅ Use new settings
from llama_index.llms.openai import OpenAI  # ✅ Correct OpenAI import

import config
import qdrant_client
from llama_index.vector_stores.qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# ✅ Initialize OpenAI API (Lower cost with gpt-3.5-turbo)
Settings.llm = OpenAI.api_key = os.getenv("OPENAI_API_KEY")

# ✅ Connect to Qdrant Cloud
qdrant_client = QdrantClient(url=config.QDRANT_URL, api_key=config.QDRANT_API_KEY)

# ✅ Initialize the embedding model
embed_model = HuggingFaceEmbedding(model_name=config.EMBEDDING_MODEL)

# ✅ Set up embedding model using new Settings API
Settings.embed_model = embed_model

# ✅ Load Qdrant vector store
vector_store = QdrantVectorStore(client=qdrant_client, collection_name=config.COLLECTION_NAME)

# ✅ Load index (no need for `ServiceContext`)
index = VectorStoreIndex.from_vector_store(vector_store=vector_store)

# ✅ Query function using OpenAI for responses
def query_book(query_text):
    query_engine = index.as_query_engine(streaming=True)  # ✅ Streaming for efficiency
    response = query_engine.query(query_text)
    return response

if __name__ == "__main__":
    query_text = input("\n🔍 Enter query: ")
    response = query_book(query_text)
    print("\n📖 **Response:**\n", response)
