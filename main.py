import streamlit as st
from PIL import Image

st.set_page_config(
page_title="Main Page",
page_icon="👋",
layout="wide",
initial_sidebar_state="expanded")

#The title
st.title("Airbnb Analytics")

#The text
st.write("Introduction in process...")

image = Image.open('airbnb.webp')
st.image(image)







