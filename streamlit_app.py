import pickle
import numpy as np
import streamlit as st

# Load your trained model
with open("model_pickle2.pkl", "rb") as f:
    model = pickle.load(f)

# Load the column names
try:
    with open("model_columns.pkl", "rb") as f:
        model_columns = pickle.load(f)
except FileNotFoundError:
    st.error("Error: 'model_columns.pkl' file not found. Ensure it is in the same directory as this script.")
    st.stop()

# List of locations (replace this with actual list or dynamically load them)
locations = [
    '1st Block Jayanagar', '1st Phase JP Nagar', '2nd Phase Judicial Layout',
    '2nd Stage Nagarbhavi', '5th Block Hbr Layout', '5th Phase JP Nagar',
    '6th Phase JP Nagar', '7th Phase JP Nagar', '8th Phase JP Nagar',
    '9th Phase JP Nagar', 'AECS Layout', 'Abbigere', 'Akshaya Nagar',
    'Ambalipura', 'Ambedkar Nagar', 'Amruthahalli', 'Anandapura', 'Ananth Nagar',
    'Anekal', 'Anjanapura', 'Ardendale', 'Arekere', 'Attibele', 'BEML Layout',
    'BTM 2nd Stage', 'BTM Layout', 'Babusapalaya', 'Badavala Nagar', 'Balagere',
    'Banashankari', 'Banashankari Stage II', 'Banashankari Stage III',
    'Banashankari Stage V', 'Banashankari Stage VI', 'Banaswadi', 'Banjara Layout',
    'Bannerghatta', 'Bannerghatta Road', 'Basavangudi', 'Basaveshwara Nagar',
    'Battarahalli', 'Begur', 'Begur Road', 'Bellandur', 'Benson Town',
    'Bharathi Nagar', 'Bhoganhalli', 'Billekahalli', 'Binny Pete',
    'Bisuvanahalli', 'Bommanahalli', 'Bommasandra', 'Bommasandra Industrial Area',
    'Bommenahalli', 'Brookefield', 'Budigere', 'CV Raman Nagar', 'Chamrajpet',
    'Chandapura', 'Channasandra', 'Chikka Tirupathi', 'Chikkabanavar',
    'Chikkalasandra', 'Choodasandra', 'Cooke Town', 'Cox Town', 'Cunningham Road',
]

# Define the prediction function
def predict_price(location, sqft, bath, bhk):
    try:
        # Create input array
        x = np.zeros(len(model_columns))
        x[0] = sqft
        x[1] = bath
        x[2] = bhk
        if location in model_columns:
            loc_index = model_columns.index(location)
            x[loc_index] = 1

        # Predict the price
        prediction = model.predict([x])[0]
        return f"Predicted House Price: ₹ {round(prediction, 2)}"
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit app interface
st.title("Bangalore House Price Prediction")
st.write("Provide house details to predict the price:")

# Inputs from user
location = st.selectbox("Select Location", locations)
sqft = st.number_input("Area (sq ft)", min_value=100.0, max_value=10000.0, step=50.0)
bath = st.number_input("Number of Bathrooms", min_value=1, max_value=10, step=1)
bhk = st.number_input("Number of BHK", min_value=1, max_value=10, step=1)

# Predict button
if st.button("Predict"):
    result = predict_price(location, sqft, bath, bhk)
    st.success(result)
