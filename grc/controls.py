import pandas as pd
import os

print("========================================")
print("       GRC CONTROL MAPPING")
print("========================================")


# ------------------------------------------------
# 1. Define GRC controls
# ------------------------------------------------

controls = [

    {
        "Control ID": "CTRL-001",
        "Risk ID": "RISK-001",
        "Control": "Training Data Validation",
        "Control Description":
            "Validate training data for unexpected changes, "
            "duplicates, invalid records and suspicious labels.",
        "NIST AI RMF": "Measure",
        "Remediation":
            "Perform automated data-quality and label validation "
            "before model training.",
        "Evidence":
            "Dataset validation report and preprocessing logs",
        "Status": "Planned"
    },

    {
        "Control ID": "CTRL-002",
        "Risk ID": "RISK-002",
        "Control": "Label Integrity Verification",
        "Control Description":
            "Verify that training labels are consistent with "
            "expected data and validation rules.",
        "NIST AI RMF": "Measure",
        "Remediation":
            "Perform label consistency checks and investigate "
            "records with suspicious label mismatches.",
        "Evidence":
            "Label validation results and detection reports",
        "Status": "Planned"
    },

    {
        "Control ID": "CTRL-003",
        "Risk ID": "RISK-003",
        "Control": "Model Performance Monitoring",
        "Control Description":
            "Compare model performance against a clean baseline "
            "to identify degradation caused by data changes.",
        "NIST AI RMF": "Measure",
        "Remediation":
            "Evaluate accuracy, precision, recall and F1 score "
            "after training-data changes.",
        "Evidence":
            "Model impact analysis and evaluation results",
        "Status": "Implemented"
    },

    {
        "Control ID": "CTRL-004",
        "Risk ID": "RISK-004",
        "Control": "Detection Result Validation",
        "Control Description":
            "Evaluate poisoning detection results using known "
            "ground-truth records and detection metrics.",
        "NIST AI RMF": "Manage",
        "Remediation":
            "Review false positives and false negatives and "
            "improve detection indicators.",
        "Evidence":
            "Confusion matrix, precision, recall and F1 results",
        "Status": "Implemented"
    }
]


# ------------------------------------------------
# 2. Create DataFrame
# ------------------------------------------------

control_df = pd.DataFrame(controls)

print("\nControl mapping created successfully!")


# ------------------------------------------------
# 3. Display controls
# ------------------------------------------------

print("\n========================================")
print("          CONTROL MAPPING")
print("========================================")

print(
    control_df[
        [
            "Control ID",
            "Risk ID",
            "Control",
            "NIST AI RMF",
            "Status"
        ]
    ].to_string(index=False)
)


# ------------------------------------------------
# 4. Save control mapping
# ------------------------------------------------

os.makedirs("grc", exist_ok=True)

output_file = "grc/controls.csv"

control_df.to_csv(
    output_file,
    index=False
)

print("\nControls saved successfully!")
print("File:", output_file)


# ------------------------------------------------
# 5. NIST AI RMF summary
# ------------------------------------------------

print("\n========================================")
print("       NIST AI RMF SUMMARY")
print("========================================")

print(
    "Govern -> Establish policies, responsibilities "
    "and accountability."
)

print(
    "Map -> Identify and understand AI risks "
    "and their context."
)

print(
    "Measure -> Analyze and evaluate AI risks "
    "using evidence and metrics."
)

print(
    "Manage -> Prioritize and address identified "
    "AI risks."
)


# ------------------------------------------------
# 6. Control summary
# ------------------------------------------------

print("\n========================================")
print("          CONTROL SUMMARY")
print("========================================")

print("Total controls:", len(control_df))

print(
    "Implemented controls:",
    (control_df["Status"] == "Implemented").sum()
)

print(
    "Planned controls:",
    (control_df["Status"] == "Planned").sum()
)


print("\n========================================")
print("       DAY 20 COMPLETED")
print("========================================")