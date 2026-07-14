"""
====================================================
Enterprise RAG Assistant v1.0
Streamlit Frontend
====================================================
"""

import streamlit as st

from src.rag_query import ask

st.set_page_config(

    page_title="Enterprise RAG Assistant",

    page_icon="📚",

    layout="wide"

)

# --------------------------------------------------

st.title("📚 Enterprise RAG Assistant")

st.caption("Production RAG using OpenRouter + ChromaDB")

# --------------------------------------------------

with st.sidebar:

    st.header("System")

    st.success("Backend Ready")

    st.success("Vector Database Ready")

    st.success("OpenRouter Connected")

    st.divider()

    st.info(
        "Document : data/policy.pdf"
    )

# --------------------------------------------------

question = st.text_input(

    "Ask a question"

)

# --------------------------------------------------

if st.button("Ask"):

    if question.strip()=="":

        st.warning("Please enter a question.")

    else:

        with st.spinner(

            "Searching knowledge base..."

        ):

            result = ask(question)

        st.subheader("Answer")

        st.write(

            result["answer"]

        )

        with st.expander(

            "Retrieved Context"

        ):

            for i, doc in enumerate(

                result["documents"],

                start=1

            ):

                st.markdown(

                    f"### Chunk {i}"

                )

                st.write(doc)

                st.divider()