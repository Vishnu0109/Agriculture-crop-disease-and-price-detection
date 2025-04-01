import pickle
import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# Initialize FastAPI app
app = FastAPI()

# Load trained model
try:
    with open("model.pkl", "rb") as model_file:
        model = pickle.load(model_file)
        expected_features = model.n_features_in_  # Get expected input size
        print(f"✅ Model loaded successfully. Expected {expected_features} features.")
except Exception as e:
    print("❌ Error loading model:", e)
    model = None
    expected_features = None

# Define input schema
class FeaturesInput(BaseModel):
    features: List[float]

@app.post("/predict")
async def predict(data: FeaturesInput):
    """Predicts output using the trained model."""
    
    # Ensure model is loaded
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded")

    # Ensure correct number of features
    if len(data.features) != expected_features:
        raise HTTPException(
            status_code=400,
            detail=f"Expected {expected_features} features, but got {len(data.features)}"
        )

    # Convert input to NumPy array
    input_data = np.array(data.features).reshape(1, -1)

    # Make prediction
    try:
        prediction = model.predict(input_data)
        return {"prediction": prediction.tolist()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

