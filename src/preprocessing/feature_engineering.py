import pandas as pd
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler

# Load preprocessed dataset
file_path = "/Users/vishnu/Desktop/agri_project/datasets/processed/crop_data_cleaned.csv"
df = pd.read_csv(file_path)

# One-Hot Encoding for categorical column (Soil color)
if "Soilcolor" in df.columns:
    encoder = OneHotEncoder(sparse_output=False, drop="first")
    encoded_soil = encoder.fit_transform(df[["Soilcolor"]])
    soil_labels = encoder.get_feature_names_out(["Soilcolor"])
    df_encoded = pd.DataFrame(encoded_soil, columns=soil_labels)
    
    # Drop original column and add new one
    df = df.drop("Soilcolor", axis=1)
    df = pd.concat([df, df_encoded], axis=1)

# Normalize numeric columns
numeric_columns = df.select_dtypes(include=["number"]).columns
scaler = MinMaxScaler()
df[numeric_columns] = scaler.fit_transform(df[numeric_columns])

# Save processed dataset
df.to_csv("/Users/vishnu/Desktop/agri_project/datasets/processed/crop_data_final.csv", index=False)

print("✅ Feature Engineering Completed! Processed dataset saved.")
