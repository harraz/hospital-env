# build_vector_store.py
import os
import pandas as pd
import numpy as np
import faiss
import pickle
from langchain_openai import OpenAIEmbeddings  # Updated import

# Load the hospital summaries
df = pd.read_csv("./data/cms_transformed/hospital_summaries.csv")
summaries = df['summary'].tolist()


API_KEY = os.environ.get("OPENAI_API_KEY")
if not API_KEY:
    raise ValueError("Please set the OPENAI_API_KEY environment variable.")

# Initialize the OpenAI embeddings model

# Generate embeddings for each summary
# embeddings_list = [embeddings_model.embed_text(text) for text in summaries]
embeddings_list = embeddings_model.embed_documents(summaries)

# Convert the list to a NumPy array
embeddings_array = np.array(embeddings_list).astype("float32")

# Create a FAISS index using the dimensionality of the embeddings
dim = embeddings_array.shape[1]
index = faiss.IndexFlatL2(dim)
index.add(embeddings_array)

# Save the FAISS index and mapping for later retrieval
with open("faiss_index.pkl", "wb") as f:
    pickle.dump(index, f)
with open("summaries_mapping.pkl", "wb") as f:
    # Save a list of dictionaries, one per record, for later lookup
    pickle.dump(df[['ACO_Name', 'summary']].to_dict('records'), f)

print("FAISS index and summaries mapping saved.")
