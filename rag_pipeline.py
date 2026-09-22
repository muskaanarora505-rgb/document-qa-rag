from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM
from langchain_text_splitters import RecursiveCharacterTextSplitter


class DocumentQASystem:

    def __init__(self):

        self.embedding_model = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        self.llm = OllamaLLM(
            model="llama3.2"
        )

        self.vector_store = None

        # FAISS returns a distance score.
        # Smaller distance means the result is more relevant.
        self.max_distance = 1.2

    def process_pdf(self, pdf_path):

        loader = PyPDFLoader(pdf_path)
        pages = loader.load()

        if not pages:
            raise ValueError("No text could be extracted from the PDF.")

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=100
        )

        chunks = splitter.split_documents(pages)

        if not chunks:
            raise ValueError("The PDF does not contain readable text.")

        self.vector_store = FAISS.from_documents(
            chunks,
            self.embedding_model
        )

        return len(chunks)

    def find_relevant_chunks(self, question):

        if self.vector_store is None:
            return []

        results = self.vector_store.similarity_search_with_score(
            question,
            k=4
        )

        relevant_chunks = []

        for document, distance in results:

            if distance <= self.max_distance:
                relevant_chunks.append(document)

        return relevant_chunks

    def ask(self, question):

        documents = self.find_relevant_chunks(question)

        if not documents:

            return (
                "I could not find this information in the uploaded document.",
                []
            )

        context_parts = []

        for document in documents:

            page_number = document.metadata.get(
                "page",
                "Unknown"
            )

            context_parts.append(
                f"Page {page_number}:\n{document.page_content}"
            )

        context = "\n\n".join(context_parts)

        prompt = f"""
You answer questions about a PDF document.

Use only the information provided in the context below.

If the answer is not present in the context, say:
"I could not find this information in the uploaded document."

Do not use outside knowledge.

Context:
{context}

Question:
{question}

Answer:
"""

        answer = self.llm.invoke(prompt)

        return answer, documents
