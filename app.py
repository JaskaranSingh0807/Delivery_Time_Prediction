import streamlit as st
import pickle

# Load the model
model_path = "Delivery_rf.pkl"
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Define the prediction function
def predict_delivery_time(features):
    # Ensure features are in the right shape for the model
    print(f"Features shape: {len(features)} features")
    prediction = model[1].predict([features])  # Wrapping features in a list to make it 2D
    return prediction[0]

# Streamlit interface
st.title("Delivery Time Prediction")

# Collect user input
distance = st.number_input("Distance (km)", min_value=0.0, max_value=1000.0, value=0.0, step=0.1)
Age = st.number_input("Delivery person Age (in Years)", min_value=18.0, max_value=50.0, value=18.0, step=1.0)
Ratings = st.number_input("Delivery Person Ratings (0-5)", min_value=0.0, max_value=5.0, value=0.0, step=0.1)
order = st.selectbox("Order Type", ["Drinks", "Meal", "Snack", "Buffet"])
vehicle = st.selectbox("Vehicle Type", ["Electric Scooter", "Motorcycle", "Scooter"])

# Map order type and vehicle type to numerical values
order_Drinks = 1 if order == "Drinks" else 0
order_Meal = 1 if order == "Meal" else 0
order_Snack = 1 if order == "Snack" else 0
vehicle_Elec = 1 if vehicle == "Electric Scooter" else 0
vehicle_Motor = 1 if vehicle == "Motorcycle" else 0
vehicle_Scooter = 1 if vehicle == "Scooter" else 0

# Create a list of features for the prediction
features = [Age, Ratings, distance, order_Drinks, order_Meal, order_Snack, vehicle_Elec, vehicle_Motor, vehicle_Scooter]

# Predict and display the result
if st.button("Predict Delivery Time"):
    prediction = predict_delivery_time(features)
    st.write(f"Predicted Delivery Time: {prediction} minutes")
