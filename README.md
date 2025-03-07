# Hospital Analytics Q&A Bot

This repository contains an end-to-end pipeline for a hospital analytics question-and-answer bot built using a Retrieval-Augmented Generation (RAG) framework. The project fetches hospital data via a CMS API, preprocesses the data to extract key metrics, generates embeddings using OpenAI, builds a FAISS vector store for efficient retrieval, and leverages a language model (LLM) to generate answers based on the retrieved context. A Streamlit web app provides a user-friendly interface for querying the system.

## Features

- **Data Fetching:** Retrieves hospital data (Performance Year, Financial, and Quality Results) from a CMS API.
- **Data Preprocessing:** Extracts relevant fields and creates text summaries from the raw data.
- **Embedding & Vector Store:** Uses OpenAI embeddings to convert summaries into vectors and builds a FAISS index for fast similarity search.
- **RAG Pipeline:** Retrieves context based on a query and generates answers using a language model.
- **User Interface:** A simple Streamlit app for interactive querying.

## Project Structure
. ├── fetch_data.py # Fetches hospital data from the CMS API 
├── preprocess.py # Preprocesses data and creates text summaries
├── build_vector_store.py # Generates embeddings and builds the FAISS vector store
├── rag_pipeline.py # RAG pipeline to retrieve context and generate answers
├── app.py # Streamlit app for user interaction
├── requirements.txt # List of required Python packages
└── README.md # This file

## Requirements

- Python 3.8+
- pip
- An OpenAI API key (set as an environment variable `OPENAI_API_KEY`)

## How It Works

1. **Data Ingestion:**  
   - `fetch_data.py` downloads hospital data via the CMS API.

2. **Preprocessing:**  
   - `preprocess.py` extracts relevant columns and creates text summaries from the data.

3. **Embedding & Vector Store:**  
   - `build_vector_store.py` generates embeddings for each summary and builds a FAISS index for efficient retrieval.

4. **RAG Pipeline:**  
   - `rag_pipeline.py`:
     - Converts a user query into an embedding using `embed_query`.
     - Retrieves the most relevant summaries from the FAISS index.
     - Constructs a prompt by combining the retrieved context with the query.
     - Sends the prompt to the LLM (via `llm.invoke`) to generate an answer.

5. **User Interface:**  
   - `app.py` provides a simple Streamlit-based interface to enter queries and display answers.

## Contributing

Contributions are welcome! Feel free to fork this repository, submit pull requests, or open issues for improvements or bug fixes.

## License

This project is licensed under the MIT License.

## Acknowledgments

- [OpenAI](https://openai.com) for language model technology.
- [LangChain](https://python.langchain.com) and its community for providing tools to build LLM-based applications.
- The CMS API for providing public hospital data.
