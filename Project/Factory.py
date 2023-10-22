# importing needed libraries
import numpy as np
import pandas as pd
import plotly.express as px
import joblib

# Dataset importing
df = pd.read_csv('Project/sources/Diabetes_clean.csv', encoding='utf-8') # Cleaned dataset
# Univariate analysis
  # Categorical feature
fig1 = px.pie(df, 'gender')
fig2 = px.histogram(df, 'smoking_history', text_auto= True, color= 'smoking_history')
fig3 = px.pie(df, 'hypertension')
fig4 = px.pie(df, 'heart_disease')

  #Numerical feature
fig5 = px.box(df, 'age')
fig6 = px.box(df, 'bmi')
fig7 = px.histogram(df, 'HbA1c_level', color= 'HbA1c_level', text_auto= True, width= 2000)
fig8 = px.box(df, 'HbA1c_level')
fig9 = px.histogram(df, 'blood_glucose_level', color='blood_glucose_level', text_auto= True, width= 5000)
fig10 = px.box(df, 'blood_glucose_level')
