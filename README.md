# SpaceWhisper

SpaceWhisper is an AI-powered application that allows users to upload NASA PDF documents and ask questions about them. The application uses LLMs and NASA datasets to provide detailed answers to user queries.

## Project Purpose

The purpose of SpaceWhisper is to provide a user-friendly interface for exploring and understanding complex astrophysics concepts and data. Users can upload PDFs related to exoplanets, black holes, or Mars missions and ask deep questions about the content.

## Tech Stack

- Python
- Streamlit
- LangChain
- OpenAI

## Installation and Running

1. Clone the repository:
   ```
   git clone https://github.com/cordz-del/spacewhisper.git
   ```

2. Navigate to the project directory:
   ```
   cd spacewhisper
   ```

3. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   streamlit run main.py
   ```

## Special Notes

- Ensure you have an OpenAI API key to use the OpenAI LLM.
- For PDF processing, the application uses PyPDFLoader, which requires PyPDF2 to be installed.
- The application is designed to work with NASA datasets, but it can be extended to other domains.
