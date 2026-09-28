import pandas as pd

print("========================================")
print("       DETECTION EVALUATION")
print("========================================")

# Load detection results
print("\nLoading detection results...")

detection_file = (
    "data/detection/"
    "random_poisoning_detection_results.csv"
)

detection_df = pd.read_csv(detection_file)

# Load ground truth
print("Loading ground-truth poisoned records...")

poisoned_file = (
    "data/poisoned/"
    "imdb_train_poisoned_1pct.csv"
)

poisoned_df = pd.read_csv(poisoned_file)

# Add ground truth to detection results
detection_df["is_poisoned"] = (
    poisoned_df["is_poisoned"]
)

# Detector prediction
detection_df["detected"] = (
    detection_df["label_mismatch"]
)

print("\nTotal records:", len(detection_df))

# Calculate confusion matrix values

TP = (
    (detection_df["is_poisoned"] == True) &
    (detection_df["detected"] == True)
).sum()

FP = (
    (detection_df["is_poisoned"] == False) &
    (detection_df["detected"] == True)
).sum()

FN = (
    (detection_df["is_poisoned"] == True) &
    (detection_df["detected"] == False)
).sum()

TN = (
    (detection_df["is_poisoned"] == False) &
    (detection_df["detected"] == False)
).sum()

print("\n========================================")
print("        CONFUSION MATRIX")
print("========================================")

print("True Positives :", TP)
print("False Positives:", FP)
print("False Negatives:", FN)
print("True Negatives :", TN)

# Precision
if TP + FP > 0:
    precision = TP / (TP + FP)
else:
    precision = 0

# Recall
if TP + FN > 0:
    recall = TP / (TP + FN)
else:
    recall = 0

# F1 Score
if precision + recall > 0:
    f1 = (
        2 * precision * recall
        / (precision + recall)
    )
else:
    f1 = 0

print("\n========================================")
print("        DETECTION METRICS")
print("========================================")

print("Precision:", round(precision, 4))
print("Recall   :", round(recall, 4))
print("F1 Score :", round(f1, 4))

# Detection rate
total_poisoned = detection_df[
    "is_poisoned"
].sum()

if total_poisoned > 0:
    detection_rate = TP / total_poisoned
else:
    detection_rate = 0

print(
    "Detection Rate:",
    round(detection_rate, 4)
)

# Save evaluation results
output_file = (
    "data/detection/"
    "detection_evaluation.csv"
)

results = pd.DataFrame({
    "Metric": [
        "True Positives",
        "False Positives",
        "False Negatives",
        "True Negatives",
        "Precision",
        "Recall",
        "F1 Score",
        "Detection Rate"
    ],
    "Value": [
        TP,
        FP,
        FN,
        TN,
        precision,
        recall,
        f1,
        detection_rate
    ]
})

results.to_csv(
    output_file,
    index=False
)

print("\nEvaluation results saved to:")
print(output_file)

print("\n========================================")
print("       DAY 16 COMPLETED")
print("========================================")