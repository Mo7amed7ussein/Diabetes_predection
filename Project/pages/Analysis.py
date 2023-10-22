# import needed libraries
import streamlit as st

import sys
# Directing to Factory file path to be able to read it
sys.path.append('diabetes_predection/Project' ) # Path of Factory file file
import Factory as fy

# Dividing our analysis into tabs, each tab contains information in one dimension and many facts (sales, profit, quantity)
tab_univariate_analysis, tab_bivariate_analysis = st.tabs(['Univariate Analysis','Bivariate Analysis'])

# Univariate_analysis Tab

with tab_univariate_analysis:
    # Title of tab
    st.title('Univariate Analysis') 
    # First section
    st.header('1- Categorical Features')
    st.subheader('a- Gender')
    st.write('You can notice that the most values of the chart is Female.')
    st.plotly_chart(fy.fig1)

    st.subheader('b- smoking_history')
    st.write('You can notice that the most values of the chart is "No Info".')
    st.plotly_chart(fy.fig2)
 
    st.subheader('b- hypertension')
    st.write('You can notice that the most values of the chart is "Healthy".')
    st.plotly_chart(fy.fig3)

    st.subheader('b- heart_disease')
    st.write('You can notice that the most values of the chart is "Healthy".')
    st.plotly_chart(fy.fig4)
    
    # Second section
    st.header('1- Numerical Features')
    st.subheader('a- age')
    st.write('You can notice that the age data is normally distributed with no outliers.')
    st.plotly_chart(fy.fig5)

    st.subheader('b- Body mass index')
    st.write('You can notice that there are some outliers which are reasonable in the data and the most values is in the normal weight range.')
    st.plotly_chart(fy.fig6)
    
 
    st.subheader('b- HbA1c_level')
    st.write('You can notice that there are some outliers which are reasonable in the data.')
    st.plotly_chart(fy.fig7)
    st.plotly_chart(fy.fig8)
    
    st.subheader('b- blood_glucose_level')
    st.write('You can notice that there are some outliers which are reasonable in the data.')
    st.plotly_chart(fy.fig9)
    st.plotly_chart(fy.fig10)
    
    
# Bivariate_analysis Tab

#with tab_bivariate_analysis:
  
