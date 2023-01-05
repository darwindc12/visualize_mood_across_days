import streamlit as st
import pathlib
import plotly.express as px
import glob
from nltk.sentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()
filepaths = sorted(glob.glob("diary/*.txt"))

positivity = []
negativity = []

for file in filepaths:
    with open(file, "r", encoding="utf-8") as one_file:
        content = one_file.read()
    scores = analyzer.polarity_scores(content)
    positivity.append(scores['pos'])
    negativity.append((scores['neg']))

dates = [pathlib.Path(file).stem for file in filepaths]

st.title("Diary Tone")
st.subheader("Positivity")

pos_figure = px.line(x=dates, y=positivity, labels={"x": "Dates", "y": "Positivity"})
st.plotly_chart(pos_figure)

st.subheader("Negativity")
neg_figure = px.line(x=dates, y=negativity, labels={"x": "Dates", "y": "Negativity"})
st.plotly_chart(neg_figure)