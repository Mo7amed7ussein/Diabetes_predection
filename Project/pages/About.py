# importing needed libraries
import streamlit as st

# Page content
st.title('About Diabetes Project')
st.write('The Diabetes prediction dataset is a collection of medical and demographic data from patients, along with their diabetes status (positive or negative). The data includes features such as age, gender, body mass index (BMI), hypertension, heart disease, smoking history, HbA1c level, and blood glucose level. This dataset can be used to build machine learning models to predict diabetes in patients based on their medical history and demographic information. This can be useful for healthcare professionals in identifying patients who may be at risk of developing diabetes and in developing personalized treatment plans. Additionally, the dataset can be used by researchers to explore the relationships between various medical and demographic factors and the likelihood of developing diabetes.')
st.write('''Columns:

* **Gender**: 

* **Age**: 

* **Hypertension**: 
Effect of hypertension disease on exposure to diabetes

* **heart_disease**: 
Effect of heart disease on exposure to diabetes

* **smoking_history**: 
Effect of smoking history on exposure to diabetes

* **BMI**: 
Body mass index, if your BMI is less than 18.5, it falls within the underweight range. If your BMI is 18.5 to 24.9, it falls within the Healthy Weight range. If your BMI is 25.0 to 29.9, it falls within the overweight range. If your BMI is 30.0 or higher, it falls within the obese range

* **HbA1c_level**: 
HbA1c is the average blood glucose (sugar) levels for the last two to three months.

* **Blood_glucose_level**: 
The blood glucose level is the amount of glucose in the blood. Glucose is a sugar that comes from the foods we eat, and it's also formed and stored inside the body. It's the main source of energy for the cells of our body, and it's carried to each cell through the bloodstream''')
