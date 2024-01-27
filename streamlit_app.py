import streamlit as st
import sklearn 
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import pickle
import numpy as np
import pandas as pd

# loading the trained model
classifier = pickle.load(open('model.pkl', 'rb'))
transformer = pickle.load(open('preprocessor.pkl', 'rb'))

def predict(data):
    # Pre-processing user input
    data = pd.DataFrame(data=[data], columns=['Age', 'Sex', 'ChestPainType', 'RestingBP', 'Cholesterol', 'FastingBS',
       'RestingECG', 'MaxHR', 'ExerciseAngina', 'Oldpeak', 'ST_Slope'])
    data['Sex'] = data['Sex'].map({'Male':1, 'Female':0}).astype(int)
    data['FastingBS'] = data['FastingBS'].map({'Yes':1, 'No':0}).astype(int)
    data['ExerciseAngina'] = data['ExerciseAngina'].map({'Yes':1, 'No':0}).astype(int)
    data['ChestPainType'] = data['ChestPainType'].map({'Typical Angina':'TA', 'Atypical Angina':'ATA', 'Non-anginal Pain':'NAP', 'Asymptomatic':'ASY'})
    print(data)
    transformed_data = transformer.transform(data)
    prediction = classifier.predict(transformed_data)
    if prediction == 0:
        pred = 'You are not likely to experience a heart failure.'
    elif prediction == 1:
        pred = 'You are likely to experience a heart failure.'
    
    return pred


def main():
    st.title("Predict your chances of experiencing a heart failure.")
    st.write("Please fill in the details below and click on the 'Predict' button to know your chances of experiencing a heart failure.")
    
    age = st.slider('Age', )  # 👈 this is a widget
    resting_blood_pressure = st.slider('What is your resting blood pressure?', 0, 200, 120)
    oldpeak = st.slider('What is your oldpeak?', 0.0, 10.0, 5.0)
    serum_cholestoral = st.slider('What is your serum cholestoral level?', 0, 600, 200)
    maxHR = st.slider('What is your maximum heart rate achieved?', 0, 300, 150)
    sex = st.radio(
        "What is your Sex?",
        ["Male", "Female"]
    )
    chest_pain_type = st.radio(
        "What type is your chest pain?",
        ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"]
    )
    fasting_blood_sugar = st.radio(
        "Do you measure fasting blood sugar > 120 mg/dl?",
        ["Yes", "No"]
    )
    resting_electrocardiographic_results = st.radio(
        "What is your resting plectrocardiographic results?",
        ["Normal", "Having ST-T wave abnormality", "Showing probable or definite left ventricular hypertrophy"]
    )
    exercise_induced_angina = st.radio(
        "Do you suffer from exercise induced angina?",
        ["Yes", "No"]
    )
    slope = st.radio(
        "What is your slope of the peak exercise ST-segment?",
        ["Up", "Flat", "Down"]
    )
    heart_failure = ''
    predict_button = st.button('Predict')
    if predict_button:
        heart_failure = predict([age, sex, chest_pain_type, resting_blood_pressure, serum_cholestoral, fasting_blood_sugar, resting_electrocardiographic_results, maxHR, exercise_induced_angina, oldpeak, slope])

    st.success(heart_failure)
    
    st.write("Disclaimer: This is just a toy project prediction and not a medical advice. Please consult a doctor for any medical advice. Thank you!")

if __name__ == '__main__':
    main()