from os import getcwd, listdir, chdir, system
from os.path import splitext
import streamlit as st

chdir("../../Downloads")

getcwd()

files = listdir(getcwd())

img_path = []

for file in files[:7]:
    if splitext(file)[1] == '.jpg':
        img_path.append(file)
    elif splitext(file)[1] == '.png':
        img_path.append(file)

my_choice = st.radio(label="Select an image: ", options=img_path)

st.write(my_choice)
