import streamlit as st
import pandas as pd
import joblib

# Load Model
model = joblib.load("final_house_price_model.pkl")

st.title("🏠 House Price Prediction")

# Inputs
area = st.number_input("Area (sqft)", min_value=500, value=1500)
bedrooms = st.number_input("Bedrooms", min_value=1, value=3)
bathrooms = st.number_input("Bathrooms", min_value=1, value=2)
floors = st.number_input("Floors", min_value=1, value=2)
age = st.number_input("Age of House", min_value=0, value=10)
distance = st.number_input("Distance to City (km)", min_value=0.0, value=5.0)
parking = st.selectbox("Parking Available", ["No", "Yes"])

parking = 1 if parking == "Yes" else 0

total_rooms = bedrooms + bathrooms

price_per_sqft = st.number_input(
    "Price Per Sqft",
    min_value=0.01,
    value=0.05,
    format="%.4f"
)

if st.button("Predict Price"):

    input_data = pd.DataFrame({
        "Area_sqft": [area],
        "Bedrooms": [bedrooms],
        "Bathrooms": [bathrooms],
        "Floors": [floors],
        "Age": [age],
        "Distance_to_City": [distance],
        "Parking": [parking],
        "Total_Rooms": [total_rooms],
        "Price_per_sqft": [price_per_sqft]
    })

    prediction = model.predict(input_data)[0]

    st.success(f"🏠 Predicted House Price: {prediction:.2f} Lakhs")