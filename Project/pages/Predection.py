import streamlit as st
import pandas as pd
import joblib
import sys
# sys.path.append('diabetes_predection/Project' ) # Path of Factory file file
import Factory as fy


Inputs = fy.Inputs
Model = fy.Model
def prediction(gender, age, hypertension, heart_disease, smoking_history, bmi, HbA1c_level, blood_glucose_level):
    test_df = pd.DataFrame(columns= Inputs)
    test_df.at[0,"gender"] = gender
    test_df.at[0,"age"] = age
    test_df.at[0,"hypertension"] = hypertension
    test_df.at[0,"heart_disease"] = heart_disease
    test_df.at[0,"smoking_history"] = smoking_history
    test_df.at[0,"bmi"] = bmi
    test_df.at[0,"HbA1c_level"] = HbA1c_level
    test_df.at[0,"blood_glucose_level"] = blood_glucose_level
    
    result = Model.predict(test_df)[0]
    if result == 1:
        return 'Patient'
    if result == 0:
        return 'Healthy'

def main():
    st.title("Diabetes disease")
    gender = st.selectbox("gender" , ['Female', 'Male'])
    
    age = st.slider("age" , min_value= 0 , max_value=100, value=0, step=1)
    
    hypertension = st.selectbox("hypertension" , ['Healthy', 'Patient'])
    
    heart_disease = st.selectbox("heart_disease" , ['Healthy', 'Patient'])
    
    smoking_history = st.selectbox("smoking_history" , ['never', 'No Info', 'current', 'former'])
    
    bmi = st.slider("Body mass index" , min_value= 10 , max_value=150 , value= 10, step=1)   
    
    HbA1c_level = st.slider("HbA1c_level" , min_value= 3 , max_value=9 , value=3, step=1)
    
    blood_glucose_level = st.slider("blood_glucose_level" , min_value= 50 , max_value= 350 , value= 50, step=1)
    
    if st.button("Predict"):
        result = prediction(gender, age, hypertension, heart_disease, smoking_history, bmi, HbA1c_level, 
                            blood_glucose_level)
        st.text(f"The Test result is {result}")

if __name__ == '__main__':
    main()
