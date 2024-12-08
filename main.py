import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Airbnb Analytics",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)
# Airbnb logo
st.image("airbnb_logo.png", width=200)  

#The title
st.markdown("<h1 style='text-align: center; color: #FF5A5F;'>Welcome to Airbnb Analytics🏠</h1>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center;'>
    <p style="font-size: 18px;">Analyze Airbnb trends, explore data insights, and predict prices using this app.</p>
</div>
""", unsafe_allow_html=True)

st.write("### Select a page from the sidebar to get started:")
st.markdown("""
<ul>
    <li><b>Data Exploration</b>: Visualize Airbnb data trends and insights.</li>
    <li><b>Price Prediction</b>: Estimate prices based on property details.</li>
</ul>
""", unsafe_allow_html=True)

image = Image.open('airbnb.webp')
st.image("airbnb.webp", caption="Airbnb Analytics Dashboard", use_column_width=True)