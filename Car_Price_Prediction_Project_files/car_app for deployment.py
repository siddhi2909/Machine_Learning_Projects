import streamlit as st
import pandas as pd
import pickle



# Load model pipeline
with open('CarPriceProject.pkl', 'rb') as f:
    pipe = pickle.load(f)

st.title("🚗 Car Price Prediction App")

st.write("Fill the details below to estimate a good buying price for a used car.")

# Input fields
company = st.text_input("Company Name (e.g., Maruti, Hyundai, etc.)")
name = st.text_input("Car Model Name (e.g., Swift, i20, etc.)")
year = st.number_input("Year of Manufacture", min_value=1990, max_value=2025, step=1, value=2015)
kms_driven = st.number_input("KMs Driven", min_value=0, step=5000, value=30000)
fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "Electric", "LPG"])

# Predict button
if st.button("Predict Price"):
    # Prepare input
    columns = ["company", "name", "year", "kms_driven", "fuel_type"]
    myinput = pd.DataFrame([[company, name, year, kms_driven, fuel_type]], columns=columns)
    
    # Prediction
    try:
        result = pipe.predict(myinput)
        st.success(f"You should buy it for ~ ₹ {abs(round(result[0][0]))} lakhs")
    except Exception as e:
        st.error(f"Prediction failed: {e}")