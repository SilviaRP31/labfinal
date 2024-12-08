import streamlit as st
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="Airbnb Analytics",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.image("airbnb_logo.png", style="height: 60px;")
# Title with background and logo
st.markdown("""
<div style="display: flex; justify-content: space-between; align-items: center; background-color: #FFEDEB; padding: 10px; border-radius: 5px;">
    <h1 style="color: #FF5A5F; margin: 0;">Welcome to Airbnb Analytics🏠</h1>
</div>
""", unsafe_allow_html=True)

# Introduction
st.markdown("""
<div style='text-align: center;'>
    <p style="font-size: 18px;">Analyze Airbnb trends, explore data insights, and predict prices using this app.</p>
</div>
""", unsafe_allow_html=True)

# Navigation instructions
st.write("### Select a page from the sidebar to get started:")
st.markdown("""
<ul>
    <li><b>Data Exploration</b>: Visualize Airbnb data trends and insights.</li>
    <li><b>Price Prediction</b>: Estimate prices based on property details.</li>
</ul>
""", unsafe_allow_html=True)

st.image("airbnb_logo.png", caption="Airbnb", use_column_width=True)  # Replace with a relevant image
