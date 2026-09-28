import pandas as pd
import joblib
import os

print("========================================")
print("       POISONING DETECTION MODULE")
print("========================================")

# 1. Load poisoned dataset
print("\nLoading poisoned dataset...")

poisoned_file = "data/poisoned/imdb_train_random_1pct.csv"

df = pd.read_csv(poisoned_file)

print("Poisoned dataset:", df.shape)

# 2. Load clean TF-IDF vectorizer
print("\nLoading TF-IDF vectorizer...")

tfidf = joblib.load("models/tfidf_vectorizer.pkl")

print("TF-IDF vectorizer loaded successfully!")

# 3. Load clean baseline model
print("\nLoading clean baseline model...")

model = joblib.load("models/baseline_model.pkl")

print("Baseline model loaded successfully!")

# 4. Convert text into TF-IDF features
print("\nConverting reviews into TF-IDF features...")

X = tfidf.transform(df["text"])

print("TF-IDF shape:", X.shape)

# 5. Generate predictions
print("\nGenerating model predictions...")

predictions = model.predict(X)

df["predicted_label"] = predictions

# 6. Compare actual and predicted labels
print("\nComparing actual labels with predictions...")

df["label_mismatch"] = (
    df["label"] != df["predicted_label"]
)

# 7. Count suspicious records
suspicious_count = df["label_mismatch"].sum()

print("\n========================================")
print("       DETECTION RESULTS")
print("========================================")

print("Total records:", len(df))
print("Suspicious records:", suspicious_count)

# 8. Create detection reason
df["reason"] = "No mismatch detected"

df.loc[
    df["label_mismatch"],
    "reason"
] = "Actual label differs from model prediction"

# 9. Suspicion status
df["status"] = "Normal"

df.loc[
    df["label_mismatch"],
    "status"
] = "Suspicious"

# 10. Save detection results
os.makedirs("data/detection", exist_ok=True)

output_file = (
    "data/detection/"
    "random_poisoning_detection_results.csv"
)

df.to_csv(output_file, index=False)

print("\nDetection results saved to:")
print(output_file)

print("\n========================================")
print("       DAY 15 COMPLETED")
print("========================================")