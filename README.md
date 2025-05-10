# Harry Potter Knowledge Chatbot

A powerful RAG (Retrieval-Augmented Generation) system that allows users to query and interact with Harry Potter book content using advanced AI technologies.

## 🚀 Features

- Semantic search capabilities for Harry Potter book content
- Efficient text chunking and embedding generation
- Vector storage using Qdrant Cloud
- Real-time query processing with streaming responses
- Parallel processing for efficient data upload
- Integration with OpenAI's GPT-3.5-turbo for intelligent responses

## 🛠️ Technical Stack

- **Framework**: LlamaIndex
- **Vector Database**: Qdrant Cloud
- **Embedding Model**: sentence-transformers/all-MiniLM-L6-v2
- **LLM**: OpenAI GPT-3.5-turbo
- **Python Libraries**:
  - llama-index
  - qdrant-client
  - llama-index-embeddings-huggingface

## 📋 Prerequisites

- Python 3.x
- OpenAI API key
- Qdrant Cloud account and API key

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/Daniyal117/harry_knowledge_chatboat.git

```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure your environment:
   - Update `config.py` with your Qdrant Cloud credentials
   - Set up your OpenAI API key

## 🚀 Usage

1. Run the full pipeline:
```bash
python main.py
```

2. Query the system:
```bash
python query_engine.py
```

## 📁 Project Structure

- `main.py`: Main pipeline orchestrator
- `query_engine.py`: Query processing and response generation
- `embedding_generator.py`: Text chunking and embedding generation
- `metadata_generator.py`: Metadata processing
- `config.py`: Configuration settings
- `requirements.txt`: Project dependencies

## 🔄 Pipeline Flow

1. **Metadata Generation**: Processes and structures book content
2. **Embedding Generation**: 
   - Splits text into chunks
   - Generates embeddings
   - Uploads to Qdrant Cloud
3. **Query Processing**:
   - Processes user queries
   - Retrieves relevant content
   - Generates responses using GPT-3.5-turbo

## ⚙️ Configuration

Update the following in `config.py`:
- `QDRANT_URL`: Your Qdrant Cloud URL
- `QDRANT_API_KEY`: Your Qdrant Cloud API key
- `COLLECTION_NAME`: Name for your vector collection
- `EMBEDDING_MODEL`: Embedding model configuration

## 📝 Notes

- The system uses chunking with a size of 512 tokens and overlap of 128 tokens
- Batch processing is implemented for efficient data upload
- Streaming responses are enabled for better user experience

## 🔒 Security

- API keys and sensitive credentials are stored in configuration files
- Ensure proper security measures for API key management

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

[Add your license information here]