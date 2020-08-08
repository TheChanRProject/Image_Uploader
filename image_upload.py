import streamlit as st
from image_loader import *

st.title("See My Images")

image_name = st.file_uploader(label="Upload an image: ", type=['png', 'jpg'])

image_move(image_name)

github_upload()
