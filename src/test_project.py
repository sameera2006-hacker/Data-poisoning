import pandas as pd
import sqlite3
import os

print("========================================")
print("       AI DATA POISONING PROJECT")
print("             SYSTEM TEST")
print("========================================")


# ==========================================
# TEST 1 — DATASET
# ==========================================

print("\n[TEST 1] Dataset")

train_file = "data/processed/imdb_train_clean.csv"
test_file = "data/processed/imdb_test_clean.csv"

if os.path.exists(train_file) and os.path.exists(test_file):

    train_df = pd.read_csv(train_file)
    test_df = pd.read_csv(test_file)

    print("PASS - Training dataset exists")
    print("PASS - Testing dataset exists")
    print("Training records:", len(train_df))
    print("Testing records:", len(test_df))

else:

    print("FAIL - Dataset files missing")


# ==========================================
# TEST 2 — POISONED DATASETS
# ==========================================

print("\n[TEST 2] Poisoning Datasets")

poisoned_files = [
    "data/poisoned/imdb_train_poisoned_1pct.csv",
    "data/poisoned/imdb_train_poisoned_5pct.csv",
    "data/poisoned/imdb_train_poisoned_10pct.csv"
]

for file in poisoned_files:

    if os.path.exists(file):

        print("PASS -", file)

    else:

        print("FAIL -", file)


# ==========================================
# TEST 3 — DETECTION RESULTS
# ==========================================

print("\n[TEST 3] Detection")

detection_file = (
    "data/detection/detection_evaluation.csv"
)

if os.path.exists(detection_file):

    detection_df = pd.read_csv(detection_file)

    print("PASS - Detection evaluation exists")
    print(
        "Detection metrics:",
        len(detection_df)
    )

else:

    print("FAIL - Detection evaluation missing")


# ==========================================
# TEST 4 — MODEL IMPACT
# ==========================================

print("\n[TEST 4] Model Impact")

impact_file = (
    "data/detection/model_impact_results.csv"
)

if os.path.exists(impact_file):

    impact_df = pd.read_csv(impact_file)

    print("PASS - Model impact results exist")
    print(
        "Experiment records:",
        len(impact_df)
    )

else:

    print("FAIL - Model impact results missing")


# ==========================================
# TEST 5 — GRC RISK REGISTER
# ==========================================

print("\n[TEST 5] GRC Risk Register")

risk_file = "grc/risk_register.csv"

if os.path.exists(risk_file):

    risk_df = pd.read_csv(risk_file)

    print("PASS - Risk register exists")
    print(
        "Risk records:",
        len(risk_df)
    )

else:

    print("FAIL - Risk register missing")


# ==========================================
# TEST 6 — GRC CONTROLS
# ==========================================

print("\n[TEST 6] GRC Controls")

control_file = "grc/controls.csv"

if os.path.exists(control_file):

    control_df = pd.read_csv(control_file)

    print("PASS - Controls file exists")
    print(
        "Control records:",
        len(control_df)
    )

else:

    print("FAIL - Controls file missing")


# ==========================================
# TEST 7 — SQLITE DATABASE
# ==========================================

print("\n[TEST 7] SQLite Database")

database_file = "grc/grc_database.db"

if os.path.exists(database_file):

    connection = sqlite3.connect(
        database_file
    )

    cursor = connection.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM risks"
    )

    risk_count = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM controls"
    )

    control_count = cursor.fetchone()[0]

    connection.close()

    print("PASS - SQLite database exists")
    print("Database risks:", risk_count)
    print("Database controls:", control_count)

else:

    print("FAIL - SQLite database missing")


# ==========================================
# TEST 8 — MODEL FILES
# ==========================================

print("\n[TEST 8] Saved Model Files")

model_file = "models/baseline_model.pkl"
vectorizer_file = "models/tfidf_vectorizer.pkl"

if os.path.exists(model_file):

    print("PASS - Baseline model exists")

else:

    print("FAIL - Baseline model missing")


if os.path.exists(vectorizer_file):

    print("PASS - TF-IDF vectorizer exists")

else:

    print("FAIL - TF-IDF vectorizer missing")


# ==========================================
# FINAL RESULT
# ==========================================

print("\n========================================")
print("          TESTING COMPLETE")
print("========================================")

print("\nThe project components were checked.")

print("\n========================================")
print("          DAY 23 TEST COMPLETE")
print("========================================")