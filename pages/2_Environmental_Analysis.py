import streamlit as st
import pandas as pd
import requests

# Load Dataset
df = pd.read_csv("final_outbreak_analysis (4).csv")

st.title("🌍 Environmental Analysis")

# ==========================
# CITY COORDINATES
# ==========================

city_coords = {

    "Mumbai": [19.0760, 72.8777],
    "Delhi": [28.7041, 77.1025],
    "Bangalore": [12.9716, 77.5946],
    "Chennai": [13.0827, 80.2707],
    "Hyderabad": [17.3850, 78.4867],
    "Kolkata": [22.5726, 88.3639],
    "Pune": [18.5204, 73.8567],
    "Ahmedabad": [23.0225, 72.5714],
    "Jaipur": [26.9124, 75.7873],
    "Lucknow": [26.8467, 80.9462],
    "Indore": [22.7196, 75.8577]
}

# ==========================
# WEATHER FUNCTION
# ==========================


def get_weather(lat, lon):

    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}"
        f"&longitude={lon}"
        f"&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
        f"&daily=temperature_2m_max,relative_humidity_2m_mean"
        f"&forecast_days=7"
    )

    response = requests.get(url)

    return response.json()
def get_aqi(lat, lon):

    url = (
        f"https://air-quality-api.open-meteo.com/v1/air-quality"
        f"?latitude={lat}"
        f"&longitude={lon}"
        f"&current=us_aqi"
    )

    response = requests.get(url)

    return response.json()
# ==========================
# CITY SELECTION
# ==========================

selected_city = st.selectbox(
    "Select City",
    list(city_coords.keys())
)

lat, lon = city_coords[selected_city]

# ==========================
# LIVE WEATHER
# ==========================

st.subheader(
    f"🌦️ Live Weather - {selected_city}"
)

weather = get_weather(lat, lon)

current = weather["current"]

col1, col2, col3 = st.columns(3)

col1.metric(
    "Temperature",
    f"{current['temperature_2m']} °C"
)

col2.metric(
    "Humidity",
    f"{current['relative_humidity_2m']} %"
)

col3.metric(
    "Wind Speed",
    f"{current['wind_speed_10m']} km/h"
)

# ==========================
# LIVE AQI
# ==========================

aqi_data = get_aqi(lat, lon)

aqi = aqi_data["current"]["us_aqi"]

st.subheader(
    f"🌫️ Live Air Quality - {selected_city}"
)

if aqi <= 50:
    category = "Good"
    st.success(f"AQI: {aqi} ({category})")

elif aqi <= 100:
    category = "Moderate"
    st.warning(f"AQI: {aqi} ({category})")

elif aqi <= 150:
    category = "Unhealthy for Sensitive Groups"
    st.warning(f"AQI: {aqi} ({category})")

else:
    category = "Unhealthy"
    st.error(f"AQI: {aqi} ({category})")

# ==========================
# 7-DAY FORECAST
# ==========================

st.subheader(
    f"📈 7-Day Weather Forecast - {selected_city}"
)

forecast_df = pd.DataFrame({
    "Date": weather["daily"]["time"],
    "Temperature": weather["daily"]["temperature_2m_max"],
    "Humidity": weather["daily"]["relative_humidity_2m_mean"]
})

st.write("Temperature Forecast")

st.line_chart(
    forecast_df.set_index("Date")["Temperature"]
)

st.write("Humidity Forecast")

st.line_chart(
    forecast_df.set_index("Date")["Humidity"]
)

# ==========================
# DATASET ANALYSIS
# ==========================

st.subheader("Environmental Factors From Dataset")

st.write(
    "Average AQI:",
    round(df["AQI"].mean(), 2)
)

st.write(
    "Average Temperature:",
    round(df["Temperature"].mean(), 2)
)

st.write(
    "Average Humidity:",
    round(df["Humidity"].mean(), 2)
)

aqi_bins = pd.cut(
    df["AQI"],
    bins=[0, 50, 100, 150, 200, 300],
    labels=[
        "Good",
        "Moderate",
        "Poor",
        "Very Poor",
        "Hazardous"
    ]
)

st.subheader("AQI Categories")

st.bar_chart(
    aqi_bins.value_counts()
)

col1, col2, col3 = st.columns(3)

col1.metric(
    "Avg AQI",
    round(df["AQI"].mean())
)

col2.metric(
    "Avg Temp",
    round(df["Temperature"].mean())
)

col3.metric(
    "Avg Humidity",
    round(df["Humidity"].mean())
)

st.subheader("AQI Distribution")

st.bar_chart(
    df["AQI"]
)

st.subheader("Temperature Distribution")

st.line_chart(
    df["Temperature"]
)

st.subheader("Humidity Distribution")

st.line_chart(
    df["Humidity"]
)

st.markdown("---")

st.caption(
    "Live weather data provided by Open-Meteo API"
)