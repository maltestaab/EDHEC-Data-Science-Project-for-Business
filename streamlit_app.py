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
    .stApp {
        background-color: #f5f5f5;
    }
    .stTitle {
        font-size: 36px;
        font-weight: bold;
        color: #2E86C1;
        text-align: center;
    }
    .stSidebar {
        background-color: #EAECEE;
    }
    .stButton>button {
        background-color: #2E86C1;
        color: white;
        font-size: 18px;
        border-radius: 10px;
        padding: 10px;
    }
    .stSuccess {
        font-size: 24px;
        font-weight: bold;
        color: #229954;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar for Context - Cool & Engaging Description
st.sidebar.title("🚀 Smart Car Price Estimator")
st.sidebar.markdown(
    """
    ### Know Your Car’s Worth Instantly! 🚗💨  
    Ever wondered **how much your car is worth** in today’s market?  
    Or planning to buy a vehicle and want to make sure **you’re paying a fair price**?  

    With **this AI-powered Car Price Estimator**, you can quickly and **accurately predict car prices** based on essential features such as:  
    - ✅ **Manufacturer & Model**  
    - ✅ **Production Year**  
    - ✅ **Fuel Type & Engine Volume**  
    - ✅ **Mileage & Cylinders**  
    - ✅ **Transmission & Drive Type**  
    - ✅ **Color, Interior, & Extras**  

    ---
    
    📊 **How It Works:**  
    Simply enter your car’s details and let the model analyze **thousands of real-world data points**  
    to provide an instant, **data-driven price prediction**.  

    ---
    
    💡 **Why Use This Tool?**  
    - 🚗 **Buying or Selling a Car?** Ensure you’re getting a **fair market price**.  
    - 📈 **Car Enthusiast?** Compare different car features and see their impact on **resale value**.  
    - 🤔 **Curious?** Play around with different configurations and discover how specs affect pricing!  

    ---
    
    🚀 **Try it now and make informed car pricing decisions with confidence!**  
    """,
    unsafe_allow_html=True,
)


# Main Title
st.markdown('<p class="stTitle">Car Price Prediction 🚙</p>', unsafe_allow_html=True)

# Dropdown options
CATEGORY_OPTIONS = ['Jeep', 'Hatchback', 'Sedan', 'Microbus', 'Goods wagon',
                    'Universal', 'Coupe', 'Minivan', 'Cabriolet', 'Limousine', 'Pickup']

FUEL_TYPE_OPTIONS = ['Hybrid', 'Petrol', 'Diesel', 'CNG', 'Plug-in Hybrid', 'LPG', 'Hydrogen']

GE