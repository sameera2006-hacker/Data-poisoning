import pandas as pd
import random
import os

print("========================================")
print("       DATA POISONING EXPERIMENT")
print("========================================")

print("\nLoading clean training dataset...")

train_df = pd.read_csv(
    "data/processed/imdb_train_clean.csv"
)

print("Training data:", train_df.shape)

os.makedirs("data/poisoned", exist_ok=True)

poisoning_levels = [0.01, 0.05, 0.10]

random.seed(42)

for poisoning_percentage in poisoning_levels:

    print("\n----------------------------------------")
    print(
        "Poisoning level:",
        poisoning_percentage * 100,
        "%"
    )
    print("----------------------------------------")

    poisoned_df = train_df.copy()

    num_records = len(poisoned_df)

    num_poisoned = int(
        num_records * poisoning_percentage
    )

    print("Total records:", num_records)
    print("Records to poison:", num_poisoned)

    poison_indices = random.sample(
        list(poisoned_df.index),
        num_poisoned
    )

    # Create ground-truth column
    poisoned_df["is_poisoned"] = False

    for index in poison_indices:

        original_label = poisoned_df.loc[
            index, "label"
        ]

        poisoned_df.loc[
            index, "label"
        ] = 1 - original_label

        poisoned_df.loc[
            index, "is_poisoned"
        ] = True

    percentage_text = int(
        poisoning_percentage * 100
    )

    output_file = (
        f"data/poisoned/"
        f"imdb_train_poisoned_"
        f"{percentage_text}pct.csv"
    )

    poisoned_df.to_csv(
        output_file,
        index=False
    )

    print("Saved:", output_file)

    print(
        "Ground-truth poisoned records:",
        poisoned_df["is_poisoned"].sum()
    )

print("\n========================================")
print("   POISONING EXPERIMENT COMPLETE")
print("========================================")