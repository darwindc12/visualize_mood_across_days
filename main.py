import streamlit as st
import pathlib
import plotly.express as px
import glob

filepaths = glob.glob("diary/*.txt")

for file in filepaths:
    with open(file, "r") as file:
        content = file.readlines()
        print(content)