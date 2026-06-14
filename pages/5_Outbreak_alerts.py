import streamlit as st
import pandas as pd

df = pd.read_csv("final_outbreak_analysis (4).csv")

st.title("🚨 Outbreak Alerts")

st.write(
    "Automated detection of potential outbreak conditions based on reported cases."
)

# Threshold for alerts
ALERT_THRESHOLD = 5

alerts = (
    df.groupby(["Location", "Disease"])
      .agg({
          "AQI": "mean",
          "Tweet_Count": "mean"
      })
      .reset_index()
)

case_counts = (
    df.groupby(["Location", "Disease"])
      .size()
      .reset_index(name="Cases")
)

alerts = alerts.merge(
    case_counts,
    on=["Location", "Disease"]
)
alerts["Outbreak_Score"] = (
    alerts["Cases"] * 10
    + alerts["AQI"] * 0.1
    + alerts["Tweet_Count"] * 0.01
)
def get_risk(score):

    if score >= 120:
        return "High"

    elif score >= 80:
        return "Medium"

    else:
        return "Low"

alerts["Risk_Level"] = alerts["Outbreak_Score"].apply(
    get_risk
)

all_alerts = alerts.copy()

high_risk = len(
    all_alerts[
        all_alerts["Risk_Level"] == "High"
    ]
)

medium_risk = len(
    all_alerts[
        all_alerts["Risk_Level"] == "Medium"
    ]
)

low_risk = len(
    all_alerts[
        all_alerts["Risk_Level"] == "Low"
    ]
)

all_alerts = alerts.copy()

high_risk = len(
    all_alerts[
        all_alerts["Risk_Level"] == "High"
    ]
)

medium_risk = len(
    all_alerts[
        all_alerts["Risk_Level"] == "Medium"
    ]
)

low_risk = len(
    all_alerts[
        all_alerts["Risk_Level"] == "Low"
    ]
)

col1, col2, col3 = st.columns(3)

col1.metric("🔴 High Risk", high_risk)
col2.metric("🟡 Medium Risk", medium_risk)
col3.metric("🟢 Low Risk", low_risk)

alerts = alerts[
    alerts["Risk_Level"] == "High"
]


if len(alerts) == 0:

    st.success(
        "No active outbreak alerts detected."
    )

else:

    st.error(
        f"{len(alerts)} active outbreak alerts detected."
    )

    for _, row in alerts.iterrows():

        st.subheader(
            f"🔴 {row['Disease']} Alert"
        )

        st.write(
            f"📍 Location: {row['Location']}"
        )

        st.write(
            f"🦠 Cases Reported: {row['Cases']}"
        )
        st.write(
            f"🚨 Outbreak Score: {row['Outbreak_Score']:.1f}"
)


        if row["Disease"] == "Malaria":

            st.info("""
Recommended Actions:
• Increase mosquito control
• Remove stagnant water
• Conduct awareness campaigns
""")

        elif row["Disease"] == "COVID-19":

            st.info("""
Recommended Actions:
• Increase testing
• Monitor hospital capacity
• Promote hygiene measures
""")

        elif row["Disease"] == "Dengue":

            st.info("""
Recommended Actions:
• Reduce mosquito breeding sites
• Monitor fever cases
• Improve surveillance
""")

        else:

            st.info("""
Recommended Actions:
• Monitor situation closely
• Increase public awareness
• Strengthen healthcare readiness
""")

        st.markdown("---")