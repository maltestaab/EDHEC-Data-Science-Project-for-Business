import streamlit as st
import requests

# Render API URL (Update with your actual Render URL)
API_URL = "https://edhec-data-science-project-for-business.onrender.com/"

st.title("Car Price Prediction")

# Create input fields
manufacturer = st.text_input("Manufacturer", "Toyota")
model = st.text_input("Model", "Corolla")
prod_year = st.number_input("Production Year", min_value=1990, max_value=2025, value=2018)
category = st.text_input("Category", "Sedan")
leather_interior = st.radio("Leather Interior", ["Yes", "No"])
fuel_type = st.text_input("Fuel Type", "Petrol")
gear_box_type = st.text_input("Gear Box Type", "Automatic")
drive_wheels = st.text_input("Drive Wheels", "Front")
doors = st.number_input("Doors", min_value=2, max_value=6, value=4)
wheel = st.radio("Wheel Position", ["Left", "Right"])
color = st.text_input("Color", "White")
turbo = st.radio("Turbo", ["Yes", "No"])
mileage = st.number_input("Mileage (km)", min_value=0, value=50000)
cylinders = st.number_input("Cylinders", min_value=2, max_value=16, value=4)
airbags = st.number_input("Airbags", min_value=0, max_value=10, value=6)
engine_volume = st.number_input("Engine Volume (cc)", min_value=500, max_value=8000, value=1800)

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

