import streamlit as st
from image_loader import *

st.title("See My Images")

name = st.text_input("Type in a file name: ")

if name != '':
    image_move(name)
    github_upload()
