import streamlit as st
from os import getcwd, listdir, chdir, system

def github_upload():

    message = st.text_input("Create a commit message: ")
    system("git add .")
    system("git commit -m '{}'".format(message))
    system('git push')


def image_move(name):
    system(f"cp ../../Downloads/{name} images/")
