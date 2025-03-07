# Hospital Analytics Q&A Bot

This repository contains an end-to-end pipeline for a hospital analytics question-and-answer bot built using a Retrieval-Augmented Generation (RAG) framework. The project fetches hospital data via a CMS API, preprocesses the data to extract key metrics, generates embeddings using OpenAI, builds a FAISS vector store for efficient retrieval, and leverages a language model (LLM) to generate answers based on the retrieved context. A Streamlit web app provides a user-friendly interface for querying the system.

## Data Source

The hospital data analyzed in this project is obtained from the CMS Medicare Shared Savings Program's [Performance Year Financial and Quality Results](https://data.cms.gov/medicare-shared-savings-program/performance-year-financial-and-quality-results). This public dataset provides detailed insights into hospital performance through key metrics such as:

- **Financial Results:** Metrics like Final Share Rate and Final Loss Rate, which indicate how financial performance is shared among providers under value-based care arrangements.
- **Quality Results:** Quality Scores and other measures that reflect patient outcomes and overall care quality.

These data points help evaluate hospitals' effectiveness in delivering cost-efficient, high-quality care and serve as a basis for comparative analysis and performance improvement strategies.

## Data Source

The hospital data analyzed in this project is obtained from the CMS Medicare Shared Savings Program's [Performance Year Financial and Quality Results](https://data.cms.gov/medicare-shared-savings-program/performance-year-financial-and-quality-results) dataset. This dataset provides insights into hospital performance, including both financial metrics and quality outcomes.

## Features

- **Financial Metrics:**  
  - **Final Share Rate:** Percentage of cost savings shared among providers.
  - **Final Loss Rate:** Percentage of losses an ACO is liable for in two-sided models.

- **Quality Performance:**  
  - **QualScore:** Overall health equity adjusted quality performance score.
  - **Additional Quality Measures:**  
    - **QualityID_318:** Falls screening for future fall risk.
    - **QualityID_110:** Influenza immunization rates.
    - **QualityID_226:** Tobacco use screening and cessation intervention.
    - **QualityID_001_WI:** Diabetes control (HbA1c >9%).

- **Patient Experience (CAHPS):**  
  - **CAHPS_1:** Getting timely care, appointments, and information.
  - **CAHPS_2:** Communication effectiveness of providers.
  - **CAHPS_3:** Overall patient rating of providers.
  - **CAHPS_4:** Access to specialists.

## Example Prompt Questions

Here are some sample questions that a hospital administrator might ask using this system:

1. **"Which hospital has the lowest 30-day readmission rate (Measure_479) and how does its financial performance (Final Share Rate and Final Loss Rate) compare to others?"**

2. **"How do the quality measures for falls screening (QualityID_318) and diabetes control (QualityID_001_WI) correlate with unplanned admissions for patients with multiple chronic conditions (Measure_484)?"**

3. **"Provide a comparison of hospitals based on overall quality score, CAHPS patient experience measures, and readmission rates."**

4. **"What trends can be observed between patient satisfaction (CAHPS fields) and clinical quality measures, such as influenza immunization (QualityID_110) and tobacco use screening (QualityID_226)?"**

5. **"Identify hospitals that demonstrate a strong balance between high quality performance (QualScore and additional quality metrics) and low readmission rates."**


## Project Structure
```md
. ├── fetch_data.py # Fetches hospital data from the CMS API 
├── preprocess.py # Preprocesses data and creates text summaries
├── build_vector_store.py # Generates embeddings and builds the FAISS vector store
├── rag_pipeline.py # RAG pipeline to retrieve context and generate answers
├── app.py # Streamlit app for user interaction
├── requirements.txt # List of required Python packages
└── README.md # This file
```

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
