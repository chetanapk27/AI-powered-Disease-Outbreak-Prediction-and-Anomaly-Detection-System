import streamlit as st
import pandas as pd

df = pd.read_csv("final_outbreak_analysis (4).csv")

st.set_page_config(
    page_title="Disease Outbreak Prediction",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Public Health Intelligence Platform")

st.markdown("""
## Welcome

This platform analyzes public health data,
environmental factors and social media trends
to identify potential disease outbreaks and
support early warning systems.

### Available Modules

🤖 AI Prediction

🌍 Environmental Analysis

📱 Social Media Trends

🗺️ Disease Hotspots

Use the sidebar to navigate.
""")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Patients",
    len(df)
)

col2.metric(
    "Diseases Tracked",
    df["Disease"].nunique()
)

col3.metric(
    "Critical Cases",
    len(df[df["Severity"] == "High"])
)

col4.metric(
    "Locations",
    df["Location"].nunique()
)