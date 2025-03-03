import streamlit as st
import requests

# Local FastAPI API URL (update this if deploying)
API_URL = "http://127.0.0.1:8000/predict"

st.title("Car Price Prediction")

# Dropdown options
CATEGORY_OPTIONS = ['Jeep', 'Hatchback', 'Sedan', 'Microbus', 'Goods wagon',
                    'Universal', 'Coupe', 'Minivan', 'Cabriolet', 'Limousine', 'Pickup']

FUEL_TYPE_OPTIONS = ['Hybrid', 'Petrol', 'Diesel', 'CNG', 'Plug-in Hybrid', 'LPG', 'Hydrogen']

GEAR_BOX_OPTIONS = ['Automatic', 'Tiptronic', 'Variator', 'Manual']

DRIVE_WHEELS_OPTIONS = ['4x4', 'Front', 'Rear']

COLOR_OPTIONS = ['Silver', 'Black', 'White', 'Grey', 'Blue', 'Green', 'Red', 
                 'Sky blue', 'Orange', 'Yellow', 'Brown', 'Golden', 'Beige', 
                 'Carnelian red', 'Purple', 'Pink']

# Input fields
manufacturer = st.text_input("Manufacturer", "Toyota")
model = st.text_input("Model", "Corolla")
prod_year = st.number_input("Production Year", min_value=1900, max_value=2025, value=2018)

category = st.selectbox("Category", CATEGORY_OPTIONS)
leather_interior = st.radio("Leather Interior", ["Yes", "No"])
fuel_type = st.selectbox("Fuel Type", FUEL_TYPE_OPTIONS)
gear_box_type = st.selectbox("Gear Box Type", GEAR_BOX_OPTIONS)
drive_wheels = st.selectbox("Drive Wheels", DRIVE_WHEELS_OPTIONS)

doors = st.radio("Number of Doors", ["2", "4", "smaller/equal 5"])
wheel = st.radio("Wheel Position", ["Left wheel", "Right wheel"])
color = st.selectbox("Color", COLOR_OPTIONS)
turbo = st.radio("Turbo", ["Yes", "No"])

mileage = st.number_input("Mileage (km)", min_value=0, value=100000)
cylinders = st.number_input("Cylinders", min_value=1, max_value=16, value=4)
airbags = st.number_input("Airbags", min_value=0, max_value=20, value=6)
engine_volume = st.number_input("Engine Volume (cc)", min_value=0, max_value=300000, value=1800)

# Predict button
if st.button("Predict Price"):
    input_data = {
        "manufacturer": manufacturer,
        "model": model,
        "prod_year": prod_year,
        "category": category,
        "leather_interior": leather_interior,
        "fuel_type": fuel_type,
        "gear_box_type": gear_box_type,
        "drive_wheels": drive_wheels,
        "doors": doors,
        "wheel": wheel,
        "color": color,
        "turbo": turbo,
        "mileage": mileage,
        "cylinders": cylinders,
        "airbags": airbags,
        "engine_volume": engine_volume
    }

    # Send request to FastAPI
    response = requests.post(API_URL, json=input_data)
    
    if response.status_code == 200:
        result = response.json()
        st.success(f"Predicted Price: ${result['predicted_price']:.2f}")
    else:
        st.error("Error in prediction request.")
