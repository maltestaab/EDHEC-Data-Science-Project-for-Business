import pickle
import numpy as np
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from preprocessing import transform_input_data  # Import preprocessing functions

# ✅ Load the trained model
with open("model_4.pkl", "rb") as file:
    model = pickle.load(file)

# ✅ Get expected feature names from the trained model
model_features = model.feature_names_in_

# ✅ Initialize FastAPI app
app = FastAPI()

# ✅ Define the input data format using Pydantic
class InputData(BaseModel):
    manufacturer: str
    model: str
    prod_year: int
    category: str
    leather_interior: str
    fuel_type: str
    gear_box_type: str
    drive_wheels: str
    doors: int
    wheel: str
    color: str
    turbo: str  # Changed from int to str ("Yes"/"No")
    mileage: int
    cylinders: int
    airbags: int
    engine_volume: int  # Assume in liters (e.g., 1.8 -> 1800 cc)

# ✅ Root endpoint (for testing)
@app.get("/")
def home():
    return {"message": "Car Price Prediction API is running!"}

# ✅ Prediction endpoint
@app.post("/predict")
def predict(data: InputData):
    # Convert input data to dictionary
    input_dict = data.dict()

    # Preprocess input
    df = transform_input_data(input_dict, model_features)

    # Ensure correct input shape for model
    input_features = df.values

    # Make prediction
    prediction = model.predict(input_features)

    # Convert back from log scale if needed
    predicted_price = np.expm1(prediction[0])

    return {"predicted_price": float(predicted_price)}
