from qdrant_client.models import PointStruct
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.text_splitter import TokenTextSplitter

import json
import config
import uuid
import concurrent.futures
from qdrant_client import QdrantClient

# Load metadata
def embeddings_generation():
    with open("metadata.json", "r", encoding="utf-8") as f:
        metadata = json.load(f)

    # Initialize Qdrant client
    qdrant_client = QdrantClient(url=config.QDRANT_URL, api_key=config.QDRANT_API_KEY)

    # Initialize embedding model
    embed_model = HuggingFaceEmbedding(model_name=config.EMBEDDING_MODEL)

    # Use LlamaIndex SentenceSplitter for chunking
    text_splitter = TokenTextSplitter(chunk_size=512, chunk_overlap=128)

    points = []

    for entry in metadata:
        book_name = entry["book_name"]
        chapter_name = entry["chapter_name"]
        chapter_text = entry["chapter_text"]

        chunks = text_splitter.split_text(chapter_text)

        for chunk in chunks:
            # Generate embedding for chunk
            vector = embed_model.get_text_embedding(chunk)  # ✅ Ensure list format

            # Store each chunk separately in Qdrant
            points.append(
                PointStruct(
                    id=str(uuid.uuid4()),  # ✅ Unique ID for each chunk
                    vector=vector,
                    payload={
                        "book": book_name,
                        "chapter": chapter_name,
                        "text": chunk,  # Store chunk text for retrieval
                    },
                )
            )

    # ✅ Upload embeddings in parallel using multithreading
    
    def upload_batch(start_idx):
        end_idx = min(start_idx + batch_size, len(points))
        qdrant_client.upsert(collection_name=config.COLLECTION_NAME, points=points[start_idx:end_idx])
        print(f"✅ Uploaded {end_idx} embeddings...")

    batch_size = 100  # Adjust batch size based on performance

    # Use ThreadPoolExecutor for parallel uploads
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:  # Adjust `max_workers` based on system capability
        print("Uploading data on the QDrant DB")
        futures = [executor.submit(upload_batch, i) for i in range(0, len(points), batch_size)]
        concurrent.futures.wait(futures)  # Wait for all threads to complete

    print(f"✅ {len(points)} embeddings stored in Qdrant Cloud with chunking!")

    return
