import streamlit as st
import pandas as pd
import joblib

st.sidebar.title("🏥 Public Health Intelligence Platform")

st.sidebar.info("""
AI-powered Disease Outbreak Prediction
and Anomaly Detection System
""")

df = pd.read_csv("final_outbreak_analysis (4).csv")

model = joblib.load(
    "disease_prediction_model.pkl"
)

st.title("🤖 AI Hospital Admission Prediction")
st.header("AI Hospital Admission Prediction")

st.caption(
    "Provide patient information to receive an AI-powered hospital admission prediction."
)

age = st.number_input(
    "Age",
    min_value=1,
    max_value=100
)

gender = st.selectbox(
    "Gender",
    ["Female", "Male"]
)

disease = st.selectbox(
    "Disease",
    df["Disease"].unique()
)

severity = st.selectbox(
    "Severity",
    df["Severity"].unique()
)

location = st.selectbox(
    "Location",
    df["Location"].unique()
)

gender_encoded = 1 if gender == "Male" else 0

disease_encoded = list(df["Disease"].unique()).index(disease)

severity_encoded = list(df["Severity"].unique()).index(severity)

location_encoded = list(df["Location"].unique()).index(location)

recommendations = {

    "Malaria": [
        "Use mosquito protection measures",
        "Avoid stagnant water exposure",
        "Monitor fever and chills"
    ],

    "COVID-19": [
        "Monitor respiratory symptoms",
        "Follow hygiene practices",
        "Avoid close contact when symptomatic"
    ],

    "Dengue": [
        "Stay hydrated",
        "Monitor fever levels",
        "Reduce mosquito exposure"
    ],

    "Typhoid": [
        "Drink safe water",
        "Maintain food hygiene",
        "Monitor digestive symptoms"
    ],

    "Flu": [
        "Rest adequately",
        "Stay hydrated",
        "Monitor symptoms"
    ],

    "Asthma": [
        "Avoid pollution exposure",
        "Monitor breathing difficulty",
        "Follow prescribed treatment plans"
    ]
}

if st.button("Predict Admission"):

    input_data = [[
        age,
        gender_encoded,
        disease_encoded,
        severity_encoded,
        location_encoded
    ]]

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0]
    confidence = max(probability) * 100
    
    st.metric(
    "Prediction Confidence",
    f"{confidence:.2f}%"
)
    if confidence >= 80:
       st.error(f"🔴 Risk Level: High ({confidence:.2f}%)")

    elif confidence >= 60:
       st.warning(f"🟡 Risk Level: Moderate ({confidence:.2f}%)")

    else:
       st.success(f"🟢 Risk Level: Low ({confidence:.2f}%)")


    if prediction == 1:

        st.balloons()

        st.warning(
            "AI Assessment: Hospital admission may be required based on the provided information."
        )

        st.info("""
Suggested Actions:
• Seek medical evaluation
• Monitor symptoms closely
• Follow healthcare guidance
• Ensure adequate hydration and rest
""")

        st.error(
            "This prediction is for educational purposes and should not replace professional medical advice."
        )

    else:

        st.balloons()

        st.success(
            "AI Assessment: Hospital admission is unlikely based on the model prediction."
        )

        st.info("""
Suggested Actions:
• Continue monitoring symptoms
• Follow preventive health measures
• Maintain healthy habits
• Seek medical advice if symptoms worsen
""")

        st.caption(
            "This prediction is generated using a machine learning model trained on public health data."
        )

    st.subheader("Disease-Specific Recommendations")

    for item in recommendations.get(disease, []):
        st.write("•", item)

st.markdown("---")

st.caption(
    "Developed for Disease Outbreak Prediction and Anomaly Detection Project"
)