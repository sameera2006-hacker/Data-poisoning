import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

print("========================================")
print("       MODEL IMPACT ANALYSIS")
print("========================================")

# ========================================
# 1. LOAD TEST DATA
# ========================================

print("\nLoading test dataset...")

test_df = pd.read_csv(
    "data/processed/imdb_test_clean.csv"
)

X_test = test_df["text"]
y_test = test_df["label"]

print("Test data:", test_df.shape)


# ========================================
# 2. LOAD CLEAN BASELINE MODEL
# ========================================

print("\nLoading clean baseline model...")

baseline_model = joblib.load(
    "models/baseline_model.pkl"
)

baseline_tfidf = joblib.load(
    "models/tfidf_vectorizer.pkl"
)

X_test_baseline = baseline_tfidf.transform(
    X_test
)

baseline_predictions = baseline_model.predict(
    X_test_baseline
)

baseline_accuracy = accuracy_score(
    y_test,
    baseline_predictions
)

baseline_precision = precision_score(
    y_test,
    baseline_predictions
)

baseline_recall = recall_score(
    y_test,
    baseline_predictions
)

baseline_f1 = f1_score(
    y_test,
    baseline_predictions
)


print("\nClean Baseline Results:")
print(
    "Accuracy :",
    round(baseline_accuracy, 4)
)
print(
    "Precision:",
    round(baseline_precision, 4)
)
print(
    "Recall   :",
    round(baseline_recall, 4)
)
print(
    "F1 Score :",
    round(baseline_f1, 4)
)


# ========================================
# 3. POISONING LEVELS
# ========================================

poisoning_levels = [1, 5, 10]

results = []


# ========================================
# 4. TRAIN POISONED MODELS
# ========================================

for level in poisoning_levels:

    print("\n========================================")
    print(
        "Training model with",
        level,
        "% poisoned data"
    )
    print("========================================")

    poisoned_file = (
        "data/poisoned/"
        f"imdb_train_poisoned_{level}pct.csv"
    )

    poisoned_df = pd.read_csv(
        poisoned_file
    )

    X_train = poisoned_df["text"]
    y_train = poisoned_df["label"]

    print(
        "Training data:",
        poisoned_df.shape
    )

    # Create a new TF-IDF vectorizer
    tfidf = TfidfVectorizer(
        max_features=20000
    )

    X_train_tfidf = tfidf.fit_transform(
        X_train
    )

    X_test_tfidf = tfidf.transform(
        X_test
    )

    print(
        "TF-IDF shape:",
        X_train_tfidf.shape
    )

    # Train model
    model = LogisticRegression(
        max_iter=1000
    )

    model.fit(
        X_train_tfidf,
        y_train
    )

    print("Model trained successfully!")

    # Predictions
    predictions = model.predict(
        X_test_tfidf
    )

    # Metrics
    accuracy = accuracy_score(
        y_test,
        predictions
    )

    precision = precision_score(
        y_test,
        predictions
    )

    recall = recall_score(
        y_test,
        predictions
    )

    f1 = f1_score(
        y_test,
        predictions
    )

    # Performance drop compared with clean model
    accuracy_drop = (
        baseline_accuracy - accuracy
    )

    f1_drop = (
        baseline_f1 - f1
    )

    print("\nResults:")
    print(
        "Accuracy :",
        round(accuracy, 4)
    )
    print(
        "Precision:",
        round(precision, 4)
    )
    print(
        "Recall   :",
        round(recall, 4)
    )
    print(
        "F1 Score :",
        round(f1, 4)
    )

    print(
        "Accuracy drop:",
        round(accuracy_drop, 4)
    )

    print(
        "F1 drop:",
        round(f1_drop, 4)
    )

    results.append({
        "Poisoning Level": f"{level}%",
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1 Score": f1,
        "Accuracy Drop": accuracy_drop,
        "F1 Drop": f1_drop
    })


# ========================================
# 5. SAVE RESULTS
# ========================================

results_df = pd.DataFrame(results)

output_file = (
    "data/detection/"
    "model_impact_results.csv"
)

results_df.to_csv(
    output_file,
    index=False
)

print("\n========================================")
print("       MODEL IMPACT SUMMARY")
print("========================================")

print(results_df.to_string(index=False))

print("\nResults saved to:")
print(output_file)

print("\n========================================")
print("       DAY 17 COMPLETED")
print("========================================")