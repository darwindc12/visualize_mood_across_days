# Diary Tone Analyzer
This is a simple application that analyzes the tone of your daily diary using the SentimentIntensityAnalyzer from the nltk library. The application takes in text files in the diary directory, analyzes the sentiment polarity, and plots the resulting positivity and negativity over time.

# Requirements
- nltk
- streamlit
- plotly

# How to use
- Add text files to the diary directory in the format <date>.txt
- Run the script: python diary_tone.py
- The application will display two plots, one for positivity and one for negativity, over time.

# Note
The script assumes that the text files are in utf-8 encoding. If your text files have a different encoding, you will need to modify the code accordingly.
