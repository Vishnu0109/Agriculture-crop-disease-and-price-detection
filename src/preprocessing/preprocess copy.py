import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


# Load the cleaned dataset
file_path = "/Users/vishnu/Desktop/agri_project/datasets/processed/crop_data_cleaned.csv"
df = pd.read_csv(file_path)

# Define features (X) and target variable (y)
X = df.drop(columns=["label"])  # Drop the target column
y = df["label"]  # Target variable

# Split dataset into train & test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Save train-test split for future use
X_train.to_csv("/Users/vishnu/Desktop/agri_project/datasets/processed/X_train.csv", index=False)
X_test.to_csv("/Users/vishnu/Desktop/agri_project/datasets/processed/X_test.csv", index=False)
y_train.to_csv("/Users/vishnu/Desktop/agri_project/datasets/processed/y_train.csv", index=False)
y_test.to_csv("/Users/vishnu/Desktop/agri_project/datasets/processed/y_test.csv", index=False)

print("✅ Data Split Completed & Saved!")
