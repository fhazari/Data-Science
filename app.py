import pickle
import gradio as gr
import numpy as np

# Load your model
with open("model_pickle2.pkl", "rb") as f:
    model = pickle.load(f)

# List of locations (replace with your actual list of locations)
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
    # Add more locations as needed
]

# Define the prediction function
def predict_price(location, sqft, bath, bhk):
    try:
        # Identify the location index
        loc_index = np.where(X.columns == location)[0][0]
        x = np.zeros(len(X.columns))
        x[0] = sqft
        x[1] = bath
        x[2] = bhk
        if loc_index >= 0:
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
        gr.Dropdown(choices=locations, label="Location"),
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
