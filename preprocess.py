# preprocess.py
import pandas as pd

# Load the dataset
df = pd.read_csv("./data/cms_raw/hospital_data.csv")

# Select relevant columns for your analysis. Adjust these based on your domain focus.
# For example, you might focus on:
# - ACO_Name: The name of the hospital or organization.
# - Agreement_Period_Num: A proxy for performance year or period.
# - FinalShareRate: Could represent a financial metric.
# - FinalLossRate: Another financial metric.
# - QualScore: A quality metric.
selected_columns = ['ACO_Name', 'Agreement_Period_Num', 'FinalShareRate', 'FinalLossRate', 'QualScore']

# Ensure the selected columns exist in your data
for col in selected_columns:
    if col not in df.columns:
        raise ValueError(f"Column '{col}' not found in CSV header.")

df = df[selected_columns]

# Create a text summary for each row
def create_summary(row):
    return (
        f"ACO: {row['ACO_Name']}. "
        f"Period: {row['Agreement_Period_Num']}. "
        f"Final Share Rate: {row['FinalShareRate']}. "
        f"Final Loss Rate: {row['FinalLossRate']}. "
        f"Quality Score: {row['QualScore']}."
    )

df['summary'] = df.apply(create_summary, axis=1)

# Save the summaries for further processing (this CSV will be used for generating embeddings)
df[['ACO_Name', 'summary']].to_csv("./data/cms_transformed/hospital_summaries.csv", index=False)
print("Preprocessing complete. Summaries saved to hospital_summaries.csv")
