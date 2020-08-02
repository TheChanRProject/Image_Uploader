import streamlit as st
from os import getcwd

st.title("See my Images")

with open(f"{getcwd()}/urls.txt", "r") as my_file:
    for line in my_file.readlines():
        line = line.replace("\n", "")
        st.image(line, width=300, use_column_width=True)
