import streamlit as st
import pickle

# Load the model
model_path = "Delivery_rf.pkl"
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Define the prediction function
def predict_delivery_time(features):
    # Ensure features are in the right shape for the model
    prediction = model[1].predict([features])
    return prediction[0]

# Streamlit interface
st.title("Delivery Time Prediction")

# Collect user input
# Assuming the model expects specific features like 'distance', 'weight', 'traffic_conditions', etc.
distance = st.number_input("Distance (km)", min_value=0.0, max_value=1000.0, value=0.0, step=0.1)
Age = st.number_input("Delivery person Age(in Years)", min_value=18.0, max_value=50.0, value=18.0, step=1.0)
Ratings = st.number_input("Delivery Person Ratings(0-5)", min_value=0.0, max_value=5.0, value=0.0, step=0.1)
order = st.selectbox("Order Type", ["Drinks", "Meal", "Snack","Buffet"])
vehicle = st.selectbox("Vehicle Type", ["Electric Scooter", "Motorcycle", "Scooter"])
#other_feature = st.number_input("Other Feature", min_value=0.0, max_value=100.0, value=0.0, step=0.1)

# Map traffic conditions to numerical values if necessary
order_Drinks = 1 if order == "Drinks" else 0
order_Meal = 1 if order == "Meal" else 0
order_snack = 1 if order == "Snack" else 0
vehicle_Elec = 1 if vehicle == "Electric Scooter" else 0
vehicle_motor = 1 if vehicle == "Motorcycle" else 0
vehicle_scooter= 1 if vehicle == "Scooter" else 0
#traffic_conditions_numeric = traffic_conditions_map[traffic_conditions]

# Create a list of features for the prediction
features = [Age,Ratings,distance,order_Drinks,order_Meal,order_snack,vehicle_Elec,vehicle_motor,vehicle_scooter]

# Predict and display the result
if st.button("Predict Delivery Time"):
    prediction = predict_delivery_time(features)
    st.write(f"Predicted Delivery Time: {prediction[0]} minutes")


# Predict and display the result
if st.button("Predict Delivery Time"):
    prediction = predict_delivery_time(features)
    st.write(f"Predicted Delivery Time: {prediction} minutes")
