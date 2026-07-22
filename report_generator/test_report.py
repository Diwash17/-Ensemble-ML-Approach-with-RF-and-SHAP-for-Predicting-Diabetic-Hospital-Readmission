"""
Test script for patient report generation.
"""

from report_generator import generate_patient_report


patient = {
    "age": 67,
    "gender": "Female",
    "race": "Caucasian",
    "time_in_hospital": 8,
    "num_medications": 15,
    "num_inpatient": 4,
}

report = generate_patient_report(
    patient_data=patient,
    prediction="Readmitted",
    probability=87.31,
    risk_level="High",
    top_features=[
        "Number of Inpatient Visits",
        "Age",
        "Time in Hospital",
        "Number of Medications",
        "Admission Type",
    ],
)

print(report)
