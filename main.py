from fastapi import FastAPI
from pydantic import BaseModel, Field
import pickle
import numpy as np
import pandas as pd
from preprocessing import transform_input_data  # Import preprocessing functions
from fastapi.middleware.cors import CORSMiddleware


# Load the trained model
with open("model_4.pkl", "rb") as file:
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
    manufacturer: str = Field(..., example="Toyota", description="Car manufacturer")
    model: str = Field(..., example="Camry", description="Car model name")
    prod_year: int = Field(..., example=2018, description="Production year of the car")
    category: str = Field(..., example="Sedan", description="Category of the vehicle")
    leather_interior: str = Field(..., example="Yes", description="Whether the car has a leather interior (Yes/No)")
    fuel_type: str = Field(..., example="Petrol", description="Type of fuel used")
    gear_box_type: str = Field(..., example="Automatic", description="Type of gearbox")
    drive_wheels: str = Field(..., example="Front", description="Type of drive wheels (Front/Rear/All)")
    doors: int = Field(..., example=4, description="Number of doors")
    wheel: str = Field(..., example="Left wheel", description="Steering wheel position (Left/Right)")
    color: str = Field(..., example="Black", description="Exterior color")
    turbo: str = Field(..., example="No", description="Indicates if the car has a turbo (Yes/No)")
    mileage: int = Field(..., example=50000, description="Total mileage in km")
    cylinders: int = Field(..., example=4, description="Number of engine cylinders")
    airbags: int = Field(..., example=6, description="Number of airbags")
    engine_volume: int = Field(..., example=2000, description="Engine volume in cc (e.g., 1.8L -> 1800cc)")

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
