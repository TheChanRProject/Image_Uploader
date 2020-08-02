import streamlit as st
from image_loader import github_upload
from os import getcwd, listdir, system

st.title("GitHub Image Uploader")

img_path = getcwd() + "/images"

uploaded_file = st.file_uploader(label='Upload an image in png format', type=['png', 'jpg'])

system(f"mv {uploaded_file} images")

github_upload()

img_list = listdir(img_path)
raw_strings = []
for image in img_list:
    raw = f"https://raw.githubusercontent.com/TheChanRProject/Image_Uploader/master/images/{image}"
    raw_strings.append(raw)

with open("urls.txt", "w") as my_file:
    for url in raw_strings:
        my_file.write(url + "\n")

with open(f"{getcwd()}/urls.txt", "r") as my_file:
    for line in my_file.readlines():
        line = line.replace("\n", "")
        st.image(line, width=300, use_column_width=True)
