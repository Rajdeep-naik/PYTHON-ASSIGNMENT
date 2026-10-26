import os
import pandas as pd


# 1. Create a sample dataset for demonstration
def create_sample_csv(filename="student_records.csv"):
    data = {
        "Roll_No": [101, 102, 103, 104, 105, 102, 106],
        "Name": ["Aarav", "Diya", "Rohan", "Isha", "Vikram", "Diya", None],
        "Marks": [85.0, 92.0, None, 78.0, 65.0, 92.0, 88.0],
        "City": [
            "Pune",
            "Mumbai",
            "Pune",
            None,
            "Nagpur",
            "Mumbai",
            "Pune",
        ],
    }
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)


def main():
    csv_file = "student_records.csv"
    if not os.path.exists(csv_file):
        create_sample_csv(csv_file)

    # Step 1: Read CSV
    df = pd.read_csv(csv_file)
    print("--- Original Dataset ---")
    print(df)

    # Step 2: Explore Dataset
    print("\n--- head() ---")
    print(df.head())
    print("\n--- info() ---")
    df.info()
    print("\n--- describe() ---")
    print(df.describe())

    # Step 3: Handle Duplicates
    print(f"\nDuplicate rows found: {df.duplicated().sum()}")
    df_cleaned = df.drop_duplicates()

    # Step 4: Handle Missing Values
    print("\nMissing values per column:")
    print(df_cleaned.isna().sum())

    # Impute numeric column with Mean
    df_cleaned["Marks"] = df_cleaned["Marks"].fillna(df_cleaned["Marks"].mean())

    # Impute categorical column with Mode
    df_cleaned["City"] = df_cleaned["City"].fillna(df_cleaned["City"].mode()[0])

    # Drop records with missing student Name
    df_cleaned = df_cleaned.dropna(subset=["Name"])

    print("\n--- Cleaned Dataset ---")
    print(df_cleaned)

    # Step 5: Data Selection and Filtering with loc[]
    print("\n--- High Scorers (Marks >= 80) using loc[] ---")
    filtered_data = df_cleaned.loc[
        df_cleaned["Marks"] >= 80, ["Name", "Marks", "City"]
    ]
    print(filtered_data)


if __name__ == "__main__":
    main()