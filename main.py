import os
import time
from metadata_generator import metadata_generation
from embedding_generator import embeddings_generation
import query_engine

def run_pipeline():
    print("\n🚀 Running Full RAG Pipeline...\n")

    # Step 1: Generate Metadata
    print("🔹 Step 1: Generating Metadata...")
    metadata_generation()

    # Step 3: Generate Embeddings and Upload
    print("\n🔹 Step 3: Generating Embeddings and Uploading to Qdrant...")
    embeddings_generation()  # This script processes and uploads embeddings

