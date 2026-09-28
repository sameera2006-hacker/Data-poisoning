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
print("     AI DATA POISONING PROJECT")
print("        CLEAN BASELINE MODEL")
print("========================================")

# --------------------------------------------------
# 1. Load processed dataset
# --------------------------------------------------

print("\nLoading processed IMDb dataset...")

train_df = pd.read_csv("data/processed/imdb_train_clean.csv")
test_df = pd.read_csv("data/processed/imdb_test_clean.csv")

print("Training data:", train_df.shape)
print("Testing data:", test_df.shape)


# --------------------------------------------------
# 2. Separate features and labels
# --------------------------------------------------

X_train = train_df["text"]
y_train = train_df["label"]

X_test = test_df["text"]
y_test = test_df["label"]

print("\nTraining features:", X_train.shape)
print("Training labels:", y_train.shape)
print("Testing features:", X_test.shape)
print("Testing labels:", y_test.shape)


# --------------------------------------------------
# 3. Convert text into TF-IDF features
# --------------------------------------------------

print("\nConverting text into numerical features using TF-IDF...")

tfidf = TfidfVectorizer(max_features=20000)

X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test)

print("TF-IDF training shape:", X_train_tfidf.shape)
print("TF-IDF testing shape:", X_test_tfidf.shape)


# --------------------------------------------------
# 4. Train Logistic Regression model
# --------------------------------------------------

print("\nTraining Logistic Regression model...")

model = LogisticRegression(max_iter=1000)

model.fit(X_train_tfidf, y_train)

print("Logistic Regression model trained successfully!")


# --------------------------------------------------
# 5. Evaluate the clean baseline model
# --------------------------------------------------

print("\nGenerating predictions...")

y_pred = model.predict(X_test_tfidf)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("\n========================================")
print("       CLEAN BASELINE MODEL RESULTS")
print("========================================")

print("Accuracy :", round(accuracy, 4))
print("Precision:", round(precision, 4))
print("Recall   :", round(recall, 4))
print("F1 Score :", round(f1, 4))

print("========================================")


# --------------------------------------------------
# 6. Save the trained model and TF-IDF vectorizer
# --------------------------------------------------

print("\nSaving model and TF-IDF vectorizer...")

joblib.dump(model, "models/baseline_model.pkl")
joblib.dump(tfidf, "models/tfidf_vectorizer.pkl")

print("Baseline model saved successfully!")
print("TF-IDF vectorizer saved successfully!")


# --------------------------------------------------
# 7. Final message
# --------------------------------------------------

print("\n========================================")
print("       DAY 10 COMPLETED")
print("========================================")

print("Model file:")
print("models/baseline_model.pkl")

print("\nVectorizer file:")
print("models/tfidf_vectorizer.pkl")

print("\nThe clean baseline model is ready for reuse.")