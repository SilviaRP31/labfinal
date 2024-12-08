import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Airbnb Analytics",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

#The title
st.title("Welcome to Airbnb Analytics")
st.markdown("""
This application helps you analyze Airbnb data, explore trends, and predict apartment prices.
Choose a page from the sidebar to get started:
- **Data Exploration**: Visualize key insights and trends.
- **Price Prediction**: Predict prices based on property details.
""")

image = Image.open('airbnb.webp')
st.image("airbnb.webp", caption="Airbnb Analytics Dashboard", use_column_width=True)

st.write("### Get started by selecting a page from the sidebar!")