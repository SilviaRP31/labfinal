import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from sklearn.ensemble import RandomForestRegressor
import plotly.express as px


def load_model():
    with open('prediction.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

model_data = load_model()
rf_model = model_data['model']
le_neighbourhood = model_data['le_neighbourhood']
le_room_type = model_data['le_room_type']
le_city = model_data['le_city']
le_host_is_superhost = model_data['le_host_is_superhost']


st.set_page_config(
page_title="Data Exploration",
page_icon="📊",
layout="wide",
initial_sidebar_state="expanded")

st.title("Data Exploration 📊 ")
st.write("In this tab we can see the most relevant information that we can extract through the data from the visual analytics.")

# Data visualizations visualitzations from tableu
st.subheader("Data Visualizations")
