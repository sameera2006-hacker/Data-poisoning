import pandas as pd
import random
import os

print("========================================")
print("   RANDOM VS TARGETED LABEL POISONING")
print("========================================")


# --------------------------------------------------
# 1. Load clean training dataset
# --------------------------------------------------

print("\nLoading clean training dataset...")

train_df = pd.read_csv("data/processed/imdb_train_clean.csv")

print("Training data:", train_df.shape)


# --------------------------------------------------
# 2. Settings
# --------------------------------------------------

poisoning_percentage = 0.01   # 1%
target_word = "excellent"

random.seed(42)


# --------------------------------------------------
# 3. RANDOM POISONING
# --------------------------------------------------

print("\n========================================")
print("         RANDOM POISONING")
print("========================================")

random_df = train_df.copy()

num_records = len(random_df)
num_poisoned = int(num_records * poisoning_percentage)

random_indices = random.sample(
    list(random_df.index),
    num_poisoned
)

for index in random_indices:

    original_label = random_df.loc[index, "label"]

    random_df.loc[index, "label"] = 1 - original_label


random_output = (
    "data/poisoned/"
    "imdb_train_random_1pct.csv"
)

random_df.to_csv(random_output, index=False)

print("Poisoning level:", poisoning_percentage * 100, "%")
print("Records poisoned:", num_poisoned)
print("Saved:", random_output)


# --------------------------------------------------
# 4. TARGETED POISONING
# --------------------------------------------------

print("\n========================================")
print("        TARGETED POISONING")
print("========================================")

targeted_df = train_df.copy()

# Find records containing the target word
target_indices = targeted_df[
    targeted_df["text"].str.contains(
        target_word,
        case=False,
        na=False
    )
].index.tolist()

print("Target word:", target_word)
print("Matching records:", len(target_indices))


# Select up to the desired number of records
target_poison_count = min(
    num_poisoned,
    len(target_indices)
)

selected_target_indices = random.sample(
    target_indices,
    target_poison_count
)


# Flip labels
for index in selected_target_indices:

    original_label = targeted_df.loc[index, "label"]

    targeted_df.loc[index, "label"] = 1 - original_label


targeted_output = (
    "data/poisoned/"
    "imdb_train_targeted_1pct.csv"
)

targeted_df.to_csv(targeted_output, index=False)


print("Poisoning level:", poisoning_percentage * 100, "%")
print("Targeted records poisoned:", target_poison_count)
print("Saved:", targeted_output)


# --------------------------------------------------
# 5. Summary
# --------------------------------------------------

print("\n========================================")
print("             COMPARISON")
print("========================================")

print("Random poisoning:")
print("  Records poisoned:", num_poisoned)

print("\nTargeted poisoning:")
print("  Target word:", target_word)
print("  Records poisoned:", target_poison_count)

