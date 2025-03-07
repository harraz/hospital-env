# fetch_data.py
import requests
import pandas as pd

# Define the API endpoint
url = "https://data.cms.gov/data-api/v1/dataset/73b2ce14-351d-40ac-90ba-ec9e1f5ba80c/data"

# Make the GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse JSON data
    data = response.json()
    
    # Convert JSON to DataFrame (assuming data is a list of dictionaries)
    df = pd.DataFrame(data)
    
    # Save the DataFrame to a CSV file
    df.to_csv("./data/hospital_data.csv", index=False)
    print("Data successfully fetched and saved to hospital_data.csv")
else:
    print(f"Error: Received status code {response.status_code}")
