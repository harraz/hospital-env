# preprocess.py
import pandas as pd

# Load the dataset
df = pd.read_csv("./data/cms_raw/hospital_data.csv")

# Define the core fields for hospital analytics
core_fields = ['ACO_Name', 'Agreement_Period_Num', 'FinalShareRate', 'FinalLossRate', 'QualScore']

# Define additional quality measure fields
quality_fields = [
    'QualityID_318',  # Falls screening for future fall risk
    'QualityID_110',  # Influenza immunization rate
    'QualityID_226',  # Tobacco use screening and cessation intervention
    'QualityID_001_WI'  # Diabetes control (HbA1c >9%), WI
]

# Define CAHPS fields (patient experience measures)
cahps_fields = [
    'CAHPS_1',  # Timely care, appointments, and information
    'CAHPS_2',  # Provider communication effectiveness
    'CAHPS_3',  # Overall patient rating of provider
    'CAHPS_4'   # Access to specialists
]

# Define readmission fields (from metadata)
readmission_fields = [
    'Measure_479',  # Hospital-wide 30-day readmission rate
    'Measure_484'   # All-cause unplanned admissions for patients with multiple chronic conditions
]

# Combine all desired fields
selected_columns = core_fields + quality_fields + cahps_fields + readmission_fields

# Verify that all selected columns exist; if not, warn the user and drop missing ones
missing = [col for col in selected_columns if col not in df.columns]
if missing:
    print(f"Warning: The following columns are missing from the data and will be skipped: {missing}")
    selected_columns = [col for col in selected_columns if col in df.columns]

df = df[selected_columns]

# Define metadata dictionary mapping field names to human-friendly labels
metadata_dict = {
    'QualityID_318': 'Falls screening for future fall risk',
    'QualityID_110': 'Influenza immunization rate',
    'QualityID_226': 'Tobacco use screening and cessation intervention',
    'QualityID_001_WI': 'Diabetes control (HbA1c >9%)',
    'CAHPS_1': 'Timely care, appointments, and information',
    'CAHPS_2': 'Provider communication effectiveness',
    'CAHPS_3': 'Overall patient rating of provider',
    'CAHPS_4': 'Access to specialists',
    'Measure_479': 'Hospital-wide 30-day readmission rate',
    'Measure_484': 'All-cause unplanned admissions (MCC patients)',
}

# Create a text summary for each record incorporating all fields with metadata
def create_summary(row):
    summary = (
        f"ACO: {row.get('ACO_Name', 'N/A')}. "
        f"Period: {row.get('Agreement_Period_Num', 'N/A')}. "
        f"Final Share Rate: {row.get('FinalShareRate', 'N/A')}. "
        f"Final Loss Rate: {row.get('FinalLossRate', 'N/A')}. "
        f"Quality Score: {row.get('QualScore', 'N/A')}. "
    )
    
    # Append quality measure fields with human-friendly labels
    for field in quality_fields:
        label = metadata_dict.get(field, field)
        summary += f"{label} ({field}): {row.get(field, 'N/A')}. "
    
    # Append CAHPS fields with human-friendly labels
    for field in cahps_fields:
        label = metadata_dict.get(field, field)
        summary += f"{label} ({field}): {row.get(field, 'N/A')}. "
    
    # Append readmission fields with human-friendly labels
    for field in readmission_fields:
        label = metadata_dict.get(field, field)
        summary += f"{label} ({field}): {row.get(field, 'N/A')}. "
    
    return summary

df['summary'] = df.apply(create_summary, axis=1)

# Save the enriched summaries for further processing
df[['ACO_Name', 'summary']].to_csv("./data/cms_transformed/hospital_summaries.csv", index=False)
print("Preprocessing complete. Summaries saved to hospital_summaries.csv")
