# Hospital Analytics Q&A Bot

This repository contains an end-to-end pipeline for a hospital analytics question-and-answer bot built using a Retrieval-Augmented Generation (RAG) framework. The project fetches hospital data via a CMS API, preprocesses the data to extract key metrics, generates embeddings using OpenAI, builds a FAISS vector store for efficient retrieval, and leverages a language model (LLM) to generate answers based on the retrieved context. A Streamlit web app provides a user-friendly interface for querying the system.

## Features

- **Data Fetching:** Retrieves hospital data (Performance Year, Financial, and Quality Results) from a CMS API.
- **Data Preprocessing:** Extracts relevant fields and creates text summaries from the raw data.
- **Embedding & Vector Store:** Uses OpenAI embeddings to convert summaries into vectors and builds a FAISS index for fast similarity search.
- **RAG Pipeline:** Retrieves context based on a query and generates answers using a language model.
- **User Interface:** A simple Streamlit app for interactive querying.

## Project Structure
. ├── fetch_data.py # Fetches hospital data from the CMS API ├── preprocess.py # Preprocesses data and creates text summaries ├── build_vector_store.py # Generates embeddings and builds the FAISS vector store ├── rag_pipeline.py # RAG pipeline to retrieve context and generate answers ├── app.py # Streamlit app for user interaction ├── requirements.txt # List of required Python packages └── README.md # This file
