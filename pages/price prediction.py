import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from sklearn.ensemble import RandomForestRegressor


with open('prediction.pkl', 'rb') as file:
    data = pickle.load(file)

rf_model = data['model']
le_neighbourhood = data['le_neighbourhood']
le_room_type = data['le_room_type']
le_city = data['le_city']
le_host_is_superhost = data['le_host_is_superhost']


st.set_page_config(
page_title="Price Prediction",
page_icon="💰",
layout="wide",
initial_sidebar_state="expanded")

st.title("Apartment Price Analysis and Prediction App")
st.markdown("Analyze apartment prices and predict prices based on your input!")

# Sidebar for user input
st.sidebar.header("Input Parameters")
selected_city = st.sidebar.selectbox("City", le_city.classes_)
room_type = st.sidebar.selectbox("Room Type", le_room_type.classes_)
neighbourhood = st.sidebar.selectbox("Neighbourhood", le_neighbourhood.classes_)
host_is_superhost = st.sidebar.selectbox("Is Host a Superhost?", le_host_is_superhost.classes_)
accommodates = st.sidebar.slider("Number of Guests", 1, 10, 2)

# Transform user inputs for prediction
def prepare_input():
    city_encoded = le_city.transform([selected_city])[0]
    room_type_encoded = le_room_type.transform([room_type])[0]
    neighbourhood_encoded = le_neighbourhood.transform([neighbourhood])[0]
    host_is_superhost_encoded = le_host_is_superhost.transform([host_is_superhost])[0]
    return np.array([[city_encoded, accommodates, neighbourhood_encoded, room_type_encoded, host_is_superhost_encoded]])

# Prediction
input_data = prepare_input()
predicted_price = rf_model.predict(input_data)[0]

st.subheader("Predicted Price")
st.write(f"The predicted price for the apartment is: **${predicted_price:.2f}**")
