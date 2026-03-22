import streamlit as st
import joblib
import pandas as pd

# Load model
with open("model.pkl", "rb") as f:
    model = joblib.load(f)

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
import pandas as pd

# Create full input with ALL features (same as training)
input_data = pd.DataFrame(columns=model.feature_names_in_)

# Fill all with 0
input_data.loc[0] = 0

# Fill actual values
input_data.loc[0, 'reading score'] = reading_score
input_data.loc[0, 'writing score'] = writing_score

# Example encoding (you can expand later)
if gender == "male":
    input_data.loc[0, 'gender_male'] = 1

if lunch == "standard":
    input_data.loc[0, 'lunch_standard'] = 1

if test_prep == "none":
    input_data.loc[0, 'test preparation course_none'] = 1

# Predict
prediction = model.predict(input_data)
