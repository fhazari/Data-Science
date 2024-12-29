import pickle
import gradio as gr
import numpy as np
import json

# Load your model
with open("model_pickle2.pkl", "rb") as f:
    model = pickle.load(f)

# Load the column names from the JSON file
with open("columns.json", "r") as f:
    model_columns = json.load(f)

# Define the prediction function
def predict_price(location, sqft, bath, bhk):
    try:
        # Initialize a zero array based on model columns
        x = np.zeros(len(model_columns))
        x[0] = sqft
        x[1] = bath
        x[2] = bhk

        # Set the location index if the location exists in model_columns
        if location in model_columns:
            loc_index = model_columns.index(location)
            x[loc_index] = 1

        # Predict and return the price
        prediction = model.predict([x])[0]
        return f"Predicted House Price: ₹ {round(prediction, 2)}"
    except Exception as e:
        return f"Error: {str(e)}"

# Create the Gradio interface
interface = gr.Interface(
    fn=predict_price,
    inputs=[
        gr.Dropdown(choices=model_columns[3:], label="Location"),  # Exclude first 3 columns for locations
        gr.Number(label="Area (sq ft)"),
        gr.Number(label="Bathrooms"),
        gr.Number(label="BHK"),
    ],
    outputs=gr.Textbox(label="Predicted Price"),
    title="Bangalore House Price Prediction",
    description="Select the location and provide house details to predict the price."
)

# Launch the app
interface.launch()
