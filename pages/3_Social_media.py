import streamlit as st
import pandas as pd

st.sidebar.title("🏥 Public Health Intelligence Platform")

st.sidebar.info("""
AI-powered Disease Outbreak Prediction
and Anomaly Detection System
""")

df = pd.read_csv("final_outbreak_analysis (4).csv")

st.title("📱 Social Media Trends")

st.subheader("Sentiment Distribution")

st.bar_chart(
    df["Sentiment"].value_counts()
)

st.metric(
    "Average Tweet Count",
    round(df["Tweet_Count"].mean(), 2)
)

st.subheader("Tweet Count Distribution")

st.line_chart(
    df["Tweet_Count"]
)

st.subheader("Top Sentiment Counts")

st.write(
    df["Sentiment"].value_counts()
)

st.markdown("---")

st.caption(
    "Developed for Disease Outbreak Prediction and Anomaly Detection Project"
)