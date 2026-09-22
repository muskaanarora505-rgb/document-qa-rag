# Document Q&A Assistant using RAG

A Retrieval-Augmented Generation application that allows users to upload PDF documents and ask questions about their content.

## Features

- PDF document upload
- PDF text extraction
- Text chunking with overlap
- Sentence Transformer embeddings
- FAISS vector search
- Local LLM using Ollama
- Source page display
- Retrieval relevance validation
- Fallback response for unavailable information
- Streamlit interface

## Tech Stack

- Python
- LangChain
- FAISS
- Sentence Transformers
- Ollama
- Streamlit
- PyPDF

## Architecture

```text
PDF
 ↓
PyPDFLoader
 ↓
Text Chunking
 ↓
Sentence Transformer Embeddings
 ↓
FAISS Vector Store
 ↓
Similarity Search
 ↓
Relevant Context
 ↓
Ollama LLM
 ↓
Answer + Sources
```

## Installation

Create a virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Ollama Setup

Install Ollama and download the model:

```bash
ollama pull llama3.2
```

Test the model:

```bash
ollama run llama3.2
```

## Run

```bash
streamlit run app.py
```

Upload a PDF, click **Process PDF**, and then enter a question.

## How It Works

1. `PyPDFLoader` extracts text from the uploaded PDF.
2. `RecursiveCharacterTextSplitter` divides the text into smaller overlapping chunks.
3. `all-MiniLM-L6-v2` converts the chunks into vector embeddings.
4. FAISS stores the embeddings and performs similarity search.
5. The user's question is compared against the stored document chunks.
6. Relevant chunks are passed as context to the Ollama LLM.
7. The LLM generates an answer using only the retrieved context.
8. The application displays the source pages used for the answer.
9. If no sufficiently relevant chunks are found, a fallback response is returned.

## Project Structure

```text
document-qa-rag/
│
├── app.py
├── rag_pipeline.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
│
├── data/
└── screenshots/
```

## Author

**Muskaan Arora**

IIT Hyderabad
