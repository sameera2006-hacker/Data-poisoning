import pandas as pd

# Load the raw datasets
train_df = pd.read_csv("data/raw/imdb_train.csv")
test_df = pd.read_csv("data/raw/imdb_test.csv")

print("Original training data:", train_df.shape)
print("Original testing data:", test_df.shape)

# Remove duplicate rows from training data
train_df = train_df.drop_duplicates()

print("Training data after removing duplicates:", train_df.shape)

# Check missing values
print("\nMissing values in training data:")
print(train_df.isnull().sum())

print("\nMissing values in testing data:")
print(test_df.isnull().sum())

# Separate input features and labels
X_train = train_df["text"]
y_train = train_df["label"]

X_test = test_df["text"]
y_test = test_df["label"]

print("\nTraining features:", X_train.shape)
print("Training labels:", y_train.shape)

print("Testing features:", X_test.shape)
print("Testing labels:", y_test.shape)

# Save cleaned datasets
train_df.to_csv("data/processed/imdb_train_clean.csv", index=False)
test_df.to_csv("data/processed/imdb_test_clean.csv", index=False)

print("\nProcessed datasets saved successfully!")