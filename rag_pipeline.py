# rag_pipeline.py
import os
import pickle
import numpy as np
import faiss
from dotenv import load_dotenv

# Load environment variables from .env file (if present)
load_dotenv()

API_KEY = os.environ.get("OPENAI_API_KEY")
if not API_KEY:
    raise ValueError("Please set the OPENAI_API_KEY environment variable.")

# Updated imports from langchain_openai for consistency with build_vector_store.py
from langchain_openai import OpenAIEmbeddings, OpenAI

# Load the FAISS index and summaries mapping
with open("faiss_index.pkl", "rb") as f:
    index = pickle.load(f)
with open("summaries_mapping.pkl", "rb") as f:
    summaries_mapping = pickle.load(f)

# Initialize the embedding model and LLM using the API key
embeddings_model = OpenAIEmbeddings(api_key=API_KEY)
llm = OpenAI(api_key=API_KEY)

def retrieve_context(query, top_k=3):
    # Use embed_query to generate an embedding for the query
    query_embedding = embeddings_model.embed_query(query)
    query_embedding = np.array(query_embedding).astype("float32").reshape(1, -1)
    distances, indices = index.search(query_embedding, top_k)
    retrieved = [summaries_mapping[i] for i in indices[0]]
    return retrieved

def generate_answer(query):
    context = retrieve_context(query)
    context_str = " ".join([item['summary'] for item in context])
    prompt = f"Using the following hospital analytics data: {context_str}\nAnswer the following question: {query}"
    response = llm.invoke(prompt)
    return response

if __name__ == "__main__":
    user_query = input("Enter your question: ")
    answer = generate_answer(user_query)
    print("Answer:", answer)
