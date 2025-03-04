import streamlit as st
import requests

# Remote FastAPI API URL
API_URL = "https://edhec-data-science-project-for-business-1.onrender.com/predict"

# Set page title and layout
st.set_page_config(
    page_title="Car Price Prediction",
    page_icon="🚗",
    layout="wide",
)

# Custom CSS for Styling
st.markdown(
    """
    <style>
        body {
            background-color: #f5f5f5;
        }
        .stApp {
            background-color: white;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }
        .stTitle {
            color: #2E86C1;
            text-align: center;
            font-size: 32px;
            font-weight: bold;
        }
        .stMarkdown {
            color: #34495E;
            text-align: center;
        }
        .stButton>button {
            background-color: #2E86C1 !important;
            color: white !important;
            font-size: 18px;
            border-radius: 10px;
            padding: 10px;
            width: 100%;
        }
        .stSelectbox, .stNumberInput, .stTextInput {
            color: black !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar for Context
st.sidebar.title("🚀 Smart Car Price Estimator")
st.sidebar.markdown(
    """
    ### Know Your Car’s Worth Instantly! 🚗💨  
    Enter your car details, and our AI will estimate its price accurately.  

    **Key Features:**  
    - ✅ Manufacturer & Model  
    - ✅ Production Year  
    - ✅ Fuel Type & Engine Volume  
    - ✅ Mileage & Cylinders  
    - ✅ Transmission & Drive Type  
    - ✅ Color, Interior, & Extras  
    """,
    unsafe_allow_html=True,
)

# Main Title
st.markdown('<p class="stTitle">Car Price Prediction 🚙</p>', unsafe_allow_html=True)

# Dropdown options
CATEGORY_OPTIONS = ['Jeep', 'Hatchback', 'Sedan', 'Microbus', 'Goods wagon',
                    'Universal', 'Coupe', 'Minivan', 'Cabriolet', 'Limousine', 'Pickup']

FUEL_TYPE_OPTIONS = ['Hybrid', 'Petrol', 'Diesel', 'CNG', 'Plug-in Hybrid', 'LPG', 'Hydrogen']

GEAR_BOX_OPTIONS = ['Automatic', 'Tiptronic', 'Variator', 'Manual']

DRIVE_WHEELS_OPTIONS = ['4x4', 'Front', 'Rear']

COLOR_OPTIONS = ['Silver', 'Black', 'White', 'Grey', 'Blue', 'Green', 'Red',
                 'Sky blue', 'Orange', 'Yellow', 'Brown', 'Golden', 'Beige',
                 'Carnelian red', 'Purple', 'Pink']

# Two-column layout for better UX
col1, col2 = st.columns(2)

with col1:
    manufacturer = st.text_input("Manufacturer", "Toyota")
    model = st.text_input("Model", "Corolla")
    prod_year = st.number_input("Production Year", min_value=1900, max_value=2025, value=2018)
    category = st.selectbox("Category", CATEGORY_OPTIONS)
    fuel_type = st.selectbox("Fuel Type", FUEL_TYPE_OPTIONS)
    gear_box_type = st.selectbox("Gear Box Type", GEAR_BOX_OPTIONS)
    drive_wheels = st.selectbox("Drive Wheels", DRIVE_WHEELS_OPTIONS)
    leather_interior = st.selectbox("Leather Interior", ["Yes", "No"])


with col2:
    doors = st.selectbox("Number of Doors", ["2", "4", "larger/equal 5"])
    wheel = st.selectbox("Wheel Position", ["Left wheel", "Right wheel"])
    color = st.selectbox("Color", COLOR_OPTIONS)
    turbo = st.selectbox("Turbo", ["Yes", "No"])
    mileage = st.number_input("Mileage (km)", min_value=0, value=100000)
    cylinders = st.number_input("Cylinders", min_value=1, max_value=16, value=4)
    airbags = st.number_input("Airbags", min_value=0, max_value=20, value=6)
    engine_volume = st.number_input("Engine Volume (cc)", min_value=0, max_value=300000, value=1800)

# Centered Predict Button
st.markdown("<br>", unsafe_allow_html=True)
centered_button = st.columns([3, 1, 3])
with centered_button[1]:
    predict = st.button("🚘 Predict Price")

# Prediction Logic
if predict:
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
        st.markdown(f'<p class="stSuccess">Predicted Price: ${result["predicted_price"]:.2f}</p>', unsafe_allow_html=True)
    else:
        st.error("Error in prediction request. Please check the inputs or API availability.")
