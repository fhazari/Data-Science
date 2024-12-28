import pickle
import numpy as np
import streamlit as st

# Load your model
with open("model_pickle2.pkl", "rb") as f:
    model = pickle.load(f)

# Load column names
with open("model_columns.pkl", "rb") as f:
    model_columns = pickle.load(f)

# Streamlit app
st.title("Bangalore House Price Prediction")
st.write("Provide house details to predict the price.")

# Inputs
location = st.selectbox("Location", model_columns[3:])  # Locations start from index 3
sqft = st.number_input("Area (sq ft)", min_value=1)
bath = st.number_input("Bathrooms", min_value=1)
bhk = st.number_input("BHK", min_value=1)

# Predict
if st.button("Predict"):
    x = np.zeros(len(model_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if location in model_columns:
        loc_index = model_columns.index(location)
        x[loc_index] = 1
    prediction = model.predict([x])[0]
    st.write(f"Predicted House Price: ₹ {round(prediction, 2)}")
