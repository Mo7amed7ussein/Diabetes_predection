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

# Bivariate analysis
fig11 = px.histogram(data_frame=df ,x = 'age',y = 'diabetes', histfunc='avg')
fig12 = px.histogram(data_frame=df ,x = 'bmi',y = 'diabetes', histfunc='avg')
fig13 = px.histogram(data_frame=df ,x = 'HbA1c_level',y = 'diabetes', histfunc='avg', color='HbA1c_level')
fig14 = px.imshow(df.corr(), text_auto= True, height= 1000)
fig14 = px.histogram(data_frame=df ,x = 'blood_glucose_level',y = 'diabetes', histfunc='avg', color= 'blood_glucose_level')
fig15 = px.histogram(data_frame=df ,x = 'gender', color= 'diabetes')
fig16 = px.histogram(data_frame=df ,x = 'hypertension', color= 'diabetes')
fig17 = px.histogram(data_frame=df ,x = 'heart_disease', color= 'diabetes')
fig18 = px.histogram(data_frame=df ,x = 'smoking_history', color= 'diabetes')
