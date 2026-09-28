import pandas as pd
import os

print("========================================")
print("          GRC RISK REGISTER")
print("========================================")

# ------------------------------------------------
# 1. Define project risks
# ------------------------------------------------

risks = [
    {
        "Risk ID": "RISK-001",
        "Asset": "AI Training Dataset",
        "Threat": "Malicious data manipulation",
        "Vulnerability": "Insufficient data validation",
        "Risk Description": "Training data integrity may be compromised by poisoned records.",
        "Likelihood": 4,
        "Impact": 5,
        "Risk Score": 20,
        "Risk Category": "Critical",
        "Treatment": "Mitigate",
        "Status": "Open"
    },

    {
        "Risk ID": "RISK-002",
        "Asset": "Training Labels",
        "Threat": "Incorrect or manipulated labels",
        "Vulnerability": "Lack of label validation",
        "Risk Description": "Incorrect labels may cause the model to learn incorrect patterns.",
        "Likelihood": 4,
        "Impact": 4,
        "Risk Score": 16,
        "Risk Category": "High",
        "Treatment": "Mitigate",
        "Status": "Open"
    },

    {
        "Risk ID": "RISK-003",
        "Asset": "ML Model",
        "Threat": "Training-data poisoning",
        "Vulnerability": "Model sensitivity to corrupted training data",
        "Risk Description": "Poisoned training data may reduce model performance.",
        "Likelihood": 3,
        "Impact": 4,
        "Risk Score": 12,
        "Risk Category": "High",
        "Treatment": "Mitigate",
        "Status": "Open"
    },

    {
        "Risk ID": "RISK-004",
        "Asset": "Poisoning Detection System",
        "Threat": "Incorrect detection",
        "Vulnerability": "Weak detection indicators",
        "Risk Description": "The detection system may incorrectly flag normal records as suspicious.",
        "Likelihood": 4,
        "Impact": 3,
        "Risk Score": 12,
        "Risk Category": "High",
        "Treatment": "Mitigate",
        "Status": "Open"
    }
]

# ------------------------------------------------
# 2. Create DataFrame
# ------------------------------------------------

risk_df = pd.DataFrame(risks)

print("\nRisk register created successfully!")

# ------------------------------------------------
# 3. Display risk register
# ------------------------------------------------

print("\n========================================")
print("             RISK REGISTER")
print("========================================")

print(
    risk_df[
        [
            "Risk ID",
            "Risk Description",
            "Likelihood",
            "Impact",
            "Risk Score",
            "Risk Category",
            "Treatment",
            "Status"
        ]
    ].to_string(index=False)
)

# ------------------------------------------------
# 4. Create output directory if required
# ------------------------------------------------

os.makedirs("grc", exist_ok=True)

# ------------------------------------------------
# 5. Save risk register
# ------------------------------------------------

output_file = "grc/risk_register.csv"

risk_df.to_csv(
    output_file,
    index=False
)

print("\nRisk register saved successfully!")
print("File:", output_file)

# ------------------------------------------------
# 6. Summary
# ------------------------------------------------

print("\n========================================")
print("          RISK SUMMARY")
print("========================================")

print("Total risks:", len(risk_df))

print(
    "Critical risks:",
    (risk_df["Risk Category"] == "Critical").sum()
)

print(
    "High risks:",
    (risk_df["Risk Category"] == "High").sum()
)

print(
    "Moderate risks:",
    (risk_df["Risk Category"] == "Moderate").sum()
)

print(
    "Low risks:",
    (risk_df["Risk Category"] == "Low").sum()
)

print("\n========================================")
print("       DAY 19 COMPLETED")
print("========================================")