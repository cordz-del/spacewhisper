import os
import streamlit as st
from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader

def build_or_load_nasa_index(path: str = "nasa_docs") -> GPTSimpleVectorIndex:
    """
    Build or load an index of NASA or astrophysics documents.
    The 'nasa_docs' folder should contain PDFs or text files with relevant data.
    """
    index_file = "nasa_index.json"
    if os.path.exists(index_file):
        # If index already exists, load it
        index = GPTSimpleVectorIndex.load_from_disk(index_file)
    else:
        # Otherwise, read files from the folder and create a brand new index
        docs = SimpleDirectoryReader(path).load_data()
        index = GPTSimpleVectorIndex.from_documents(docs)
        index.save_to_disk(index_file)
    return index

def main():
    st.title("SpaceWhisper: Ask the Cosmos")

    st.markdown("""
    **Welcome to SpaceWhisper!**  
    This demo references local NASA documents or astrophysics PDFs.
    Type any question about exoplanets, black holes, cosmic microwave background, etc.,
    and see how the LLM responds based on the knowledge from your uploaded docs.
    """)

    # Build or load the index
    index = build_or_load_nasa_index("nasa_docs")

    # Let the user type a question
    user_question = st.text_input("Ask something about NASA missions or astrophysics:")
    
    if st.button("Get Answer"):
        if user_question.strip():
            # Query the LlamaIndex
            response = index.query(user_question)
            st.write("**Answer:**")
            st.write(response)
        else:
            st.warning("Please enter a question.")

    st.markdown("---")
    st.info("**Note**: Make sure you have the 'nasa_docs' folder with PDF or text files in the same directory.")

if __name__ == "__main__":
    main()
