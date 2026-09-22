import tempfile

import streamlit as st

from rag_pipeline import DocumentQASystem


st.set_page_config(
    page_title="Document Q&A Assistant",
    page_icon="📄"
)

st.title("📄 Document Q&A Assistant")
st.write("Upload a PDF and ask questions about its content.")


@st.cache_resource
def get_rag_system():
    return DocumentQASystem()


rag = get_rag_system()

uploaded_file = st.file_uploader(
    "Choose a PDF file",
    type=["pdf"]
)


if uploaded_file is not None:

    st.info(f"Selected file: {uploaded_file.name}")

    if st.button("Process PDF"):

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        ) as temp_file:

            temp_file.write(uploaded_file.getvalue())
            pdf_path = temp_file.name

        with st.spinner("Reading and indexing the PDF..."):

            try:
                chunk_count = rag.process_pdf(pdf_path)

                st.session_state["processed"] = True

                st.success(
                    f"PDF processed successfully ({chunk_count} chunks)."
                )

            except Exception as error:
                st.error(f"Could not process the PDF: {error}")


st.divider()

question = st.text_input(
    "Enter your question"
)


if st.button("Ask Question"):

    if uploaded_file is None:
        st.warning("Please upload a PDF first.")

    elif not st.session_state.get("processed", False):
        st.warning("Please process the PDF first.")

    elif not question.strip():
        st.warning("Please enter a question.")

    else:

        with st.spinner("Searching the document..."):

            try:
                answer, sources = rag.ask(question)

                st.subheader("Answer")
                st.write(answer)

                if sources:

                    st.subheader("Sources")

                    for number, source in enumerate(sources, 1):

                        page = source.metadata.get(
                            "page",
                            "Unknown"
                        )

                        with st.expander(
                            f"Source {number} - Page {page}"
                        ):
                            st.write(source.page_content)

            except Exception as error:
                st.error(f"Something went wrong: {error}")
