import streamlit as st
from langchain.llms import OpenAI
from langchain.document_loaders import PyPDFLoader
from langchain.indexes import VectorstoreIndexCreator

# Initialize the OpenAI LLM
llm = OpenAI()

# Function to process the uploaded PDF and create an index
@st.cache(allow_output_mutation=True)
def create_index(pdf_file):
    loader = PyPDFLoader(pdf_file)
    index = VectorstoreIndexCreator().from_loaders([loader])
    return index

# Streamlit interface
st.title("SpaceWhisper: Ask the Cosmos Anything")

# File uploader for PDF files
uploaded_file = st.file_uploader("Upload a NASA PDF document", type="pdf")

if uploaded_file is not None:
    # Create an index from the uploaded PDF
    index = create_index(uploaded_file)
    st.write("PDF processed and indexed successfully!")
    
    # Input for user questions
    question = st.text_input("Ask a question about the document:")
    if question:
        # Query the index with the user's question
        response = index.query(question, llm=llm)
        st.write("Answer:", response)
