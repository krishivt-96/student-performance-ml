import streamlit as st
import pickle
import pandas as pd

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🎓 Student Performance Predictor")

# Inputs
gender = st.selectbox("Gender", ["male", "female"])
lunch = st.selectbox("Lunch", ["standard", "free/reduced"])
test_prep = st.selectbox("Test Preparation", ["none", "completed"])
reading_score = st.slider("Reading Score", 0, 100, 50)
writing_score = st.slider("Writing Score", 0, 100, 50)

# Create input dataframe
input_data = pd.DataFrame({
    'reading score': [reading_score],
    'writing score': [writing_score],
    'gender_male': [1 if gender == "male" else 0],
    'lunch_standard': [1 if lunch == "standard" else 0],
    'test preparation course_none': [1 if test_prep == "none" else 0]
})

# Prediction
if st.button("Predict Math Score"):
    prediction = model.predict(input_data)
    st.success(f"Predicted Math Score: {round(prediction[0], 2)}")