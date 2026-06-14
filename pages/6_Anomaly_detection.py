import streamlit as st
import pandas as pd

df = pd.read_csv("final_outbreak_analysis_complete.csv")

st.title("🔍 Anomaly Detection Dashboard")

st.write(
    "Isolation Forest identifies unusual health records that may indicate potential outbreak events."
)

normal_count = len(
    df[df["Anomaly"] == 1]
)

anomaly_count = len(
    df[df["Anomaly"] == -1]
)

anomaly_percentage = (
    anomaly_count / len(df)
) * 100

st.info(
    f"{anomaly_percentage:.2f}% of records were flagged as anomalous by the Isolation Forest model."
)
col1, col2, col3 = st.columns(3)

col1.metric(
    "Normal Records",
    normal_count
)

col2.metric(
    "Anomalies Detected",
    anomaly_count
)

col3.metric(
    "Anomaly %",
    f"{anomaly_percentage:.2f}%"
)

st.subheader("Alert Distribution")

st.bar_chart(
    df["Outbreak_Alert"].value_counts()
)

st.subheader("Anomalous Records")

critical = df[
    df["Anomaly"] == -1
]

st.dataframe(
    critical[
        [
            "Patient_ID",
            "Date",
            "Symptoms",
            "Hospital_Admission",
            "AQI",
            "Temperature",
            "Humidity",
            "Tweet_Count",
            "Sentiment"
        ]
    ].head(20)
)


st.warning(
    "Records marked as anomalous may represent unusual disease activity and require further investigation."
)