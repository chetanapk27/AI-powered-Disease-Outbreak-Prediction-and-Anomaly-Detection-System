import streamlit as st
import pandas as pd
import folium

st.sidebar.title("🏥 Public Health Intelligence Platform")

st.sidebar.info("""
AI-powered Disease Outbreak Prediction
and Anomaly Detection System
""")

from streamlit_folium import st_folium

df = pd.read_csv("final_outbreak_analysis (4).csv")

st.title("🗺️ Disease Hotspots")

m = folium.Map(
    location=[22, 78],
    zoom_start=5
)

for _, row in df.iterrows():

    folium.CircleMarker(
        location=[
            row["Latitude"],
            row["Longitude"]
        ],
        radius=4,
        popup=f"""
Disease: {row['Disease']}
AQI: {row['AQI']}
Tweets: {row['Tweet_Count']}
""",
        fill=True
    ).add_to(m)

st_folium(
    m,
    width=900,
    height=600
)
st.markdown("---")

st.caption(
    "Developed for Disease Outbreak Prediction and Anomaly Detection Project"
)