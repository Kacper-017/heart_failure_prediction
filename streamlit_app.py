import streamlit as st
import pickle
import numpy as np

# loading the trained model
# classifier = pickle.load(open('model.pkl', 'rb'))
# transformer = pickle.load(open('transformer.pkl', 'rb'))

# def predict(data: list):
#     # Pre-processing user input
#     data = np.array(data)
#     transformed_data = transformer.transform(data.reshape(1, -1))
#     prediction = classifier.predict(transformed_data)
#     if prediction == 0:
#         pred = 'You are not likely to experience a heart failure.'
#     elif prediction == 1:
#         pred = 'You are likely to experience a heart failure.'
    
#     return pred


def main():
    st.title("Predict your chances of experiencing a heart failure.")
    st.write("Please fill in the details below and click on the 'Predict' button to know your chances of experiencing a heart failure.")
    
    age = st.slider('Age', )  # 👈 this is a widget
    resting_blood_pressure = st.slider('What is your resting blood pressure?', 0, 200, 120)
    oldpeak = st.slider('What is your oldpeak?', 0.0, 10.0, 5.0)
    serum_cholestoral = st.slider('What is your serum cholestoral level?', 0, 600, 200)
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
        ["Upsloping", "Flat", "Downsloping"]
    )
    heart_failure = ''
    predict_button = st.button('Predict')
    if predict_button:
        pass
        # heart_failure = predict([age, resting_blood_pressure, oldpeak, serum_cholestoral, sex, chest_pain_type, fasting_blood_sugar, resting_electrocardiographic_results, exercise_induced_angina, slope])

    st.success(heart_failure)
    
    st.write("Disclaimer: This is just a toy project prediction and not a medical advice. Please consult a doctor for any medical advice. Thank you!")

if __name__ == '__main__':
    main()