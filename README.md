#  Document Q&A Assistant using RAG

A Retrieval-Augmented Generation (RAG) based application for asking questions about PDF documents.

The project is being developed using Python, LangChain, FAISS, Ollama, and Streamlit.

## Tech Stack

* Python
* LangChain
* FAISS
* Sentence Transformers
* Ollama
* Streamlit
* PyPDF

## Current Workflow

The planned workflow is:

```text
PDF Document
     |
Text Extraction
     |
Text Chunking
     |
Embeddings
     |
FAISS Vector Search
     |
Relevant Context
     |
Ollama LLM
     |
Answer
```

## Project Structure

```text
document-qa-rag/
│
├── app.py
├── rag_pipeline.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env.example
```

## Project Status

This project is currently under development.

The main RAG pipeline and Streamlit interface are being implemented and tested.

More features and improvements will be added as development progresses.

## Author

**Muskaan Arora**

IIT Hyderabad
