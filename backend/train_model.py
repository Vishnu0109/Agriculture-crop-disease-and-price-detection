import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

# 🔹 Step 1: Generate Sample Data (71 features)
X, y = make_classification(n_samples=500, n_features=71, random_state=42)

# 🔹 Step 2: Split Data into Training & Testing Sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 🔹 Step 3: Train a Random Forest Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 🔹 Step 4: Save the Trained Model
model_path = "model.pkl"
with open(model_path, "wb") as f:
    pickle.dump(model, f)

print(f"✅ Model trained and saved at {model_path}")

