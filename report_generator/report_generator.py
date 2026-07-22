"""
Utility functions for generating patient readmission reports.
"""

from datetime import datetime


def generate_patient_report(
    patient_data: dict,
    prediction: str,
    probability: float,
    risk_level: str,
    top_features: list[str],
) -> str:
    """
    Generate a formatted patient readmission report.

    Parameters
    ----------
    patient_data : dict
        Patient information.

    prediction : str
        Predicted class.

    probability : float
        Prediction confidence (%).

    risk_level : str
        Risk category.

    top_features : list[str]
        Features that contributed most to the prediction.

    Returns
    -------
    str
        Patient report.
    """

    feature_text = "\n".join(
        f"- {feature}" for feature in top_features
    )

    return f"""
Diabetes Readmission Risk Report
Generated: {datetime.now():%d-%m-%Y %H:%M}

Patient Information
-------------------
Age: {patient_data['age']}
Gender: {patient_data['gender']}
Race: {patient_data['race']}
Time in Hospital: {patient_data['time_in_hospital']} days
Number of Medications: {patient_data['num_medications']}
Number of Inpatient Visits: {patient_data['num_inpatient']}

Prediction
----------
Prediction: {prediction}
Risk Level: {risk_level}
Probability: {probability:.2f}%

AI Summary
----------
The patient is predicted to have a {risk_level.lower()} risk of
hospital readmission.

Top Risk Factors
----------------
{feature_text}

Disclaimer

----------
This report is intended for educational and research purposes only.
It should not replace professional medical judgment.
"""
