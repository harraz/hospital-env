# app.py
import streamlit as st
from rag_pipeline import generate_answer

st.title("Hospital Analytics Q&A Bot")
st.write("Ask questions about hospital performance metrics, financial data, and quality results.")

user_query = st.text_input("Your question:")
if st.button("Submit"):
    if user_query:
        answer = generate_answer(user_query)
        st.write("**Answer:**")
        st.write(answer)
    else:
        st.write("Please enter a question.")
