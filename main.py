from fastapi import FastAPI
from pydantic import BaseModel, Field
import pickle
import numpy as np
import pandas as pd
from preprocessing import transform_input_data  # Import preprocessing functions
from fastapi.middleware.cors import CORSMiddleware


# Load the trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Get expected feature names from the trained model
model_features = model.feature_names_in_

# Initialize FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows requests from any frontend (change to specific URL for security)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

# Define the input data format using Pydantic
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
    turbo: str
    mileage: int
    cylinders: int
    airbags: int
    engine_volume: int

# Root endpoint (for testing)
@app.get("/")
def home():
    """Basic API health check."""
    return {"message": "Car Price Prediction API is running!"}

# Prediction endpoint
@app.post("/predict")
def predict(data: InputData):
    """Predict the price of a car based on input features."""
    
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
