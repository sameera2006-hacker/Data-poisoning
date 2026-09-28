from datasets import load_dataset

print("Downloading IMDb dataset...")

# Download IMDb dataset
imdb = load_dataset("stanfordnlp/imdb")

# Convert train and test to pandas
train_df = imdb["train"].to_pandas()
test_df = imdb["test"].to_pandas()

# Save CSV files
train_df.to_csv("data/raw/imdb_train.csv", index=False)
test_df.to_csv("data/raw/imdb_test.csv", index=False)

print("IMDb dataset saved successfully!")
print("Training data:", train_df.shape)
print("Testing data:", test_df.shape)