# import needed libraries
import streamlit as st

# Directing to Factory file path to be able to read it
# sys.path.append('diabetes_predection/Project' ) # Path of Factory file file
import Factory as fy

# Dividing our analysis into tabs, each tab contains information in one dimension and many facts (sales, profit, quantity)
tab_univariate_analysis, tab_bivariate_analysis = st.tabs(['Univariate Analysis','Bivariate Analysis'])

# Univariate_analysis Tab

with tab_univariate_analysis:
    # Title of tab
    st.title('Univariate Analysis') 
    # First section
    Type = st.selectbox('Choose Feature type', ('Categorical Features', 'Numerical Features'))
    if Type == 'Categorical Features':
        st.header('1- Categorical Features')
        option1 = st.selectbox('Choose the feature you want to review', ('Gender', 'Hypertension', 'Heart disease', 'Smoking history'))
        if option1 == 'Gender':
            st.subheader('a- Gender')
            st.write('You can notice that the most values of the chart is Female.')
            st.plotly_chart(fy.fig1)

        elif option1 == 'Smoking history':
            st.subheader('b- Smoking history')
            st.write('You can notice that the most values of the chart is "No Info".')
            st.plotly_chart(fy.fig2)

        elif option1 == 'Hypertension':
            st.subheader('b- Hypertension')
            st.write('You can notice that the most values of the chart is "Healthy".')
            st.plotly_chart(fy.fig3)

        else:
            st.subheader('b- Heart disease')
            st.write('You can notice that the most values of the chart is "Healthy".')
            st.plotly_chart(fy.fig4)

    # Second section
    if Type == 'Numerical Features':
        st.header('1- Numerical Features')
        option2 = st.selectbox('Choose the feature you want to review', ('Age', 'Body mass index', 'HbA1c level', 'Blood glucose level'))
        if option2 == 'Age':
            st.subheader('a- Age')
            st.write('You can notice that the age data is normally distributed with no outliers.')
            st.plotly_chart(fy.fig5)
            
        elif option2 == 'Body mass index':
            st.subheader('b- Body mass index')
            st.write('You can notice that there are some outliers which are reasonable in the data and the most values is in the normal weight range.')
            st.plotly_chart(fy.fig6)

        elif option2 == 'HbA1c level':
            st.subheader('b- HbA1c_level')
            st.write('You can notice that there are some outliers which are reasonable in the data.')
            st.plotly_chart(fy.fig7)
            st.plotly_chart(fy.fig8)

        else:
            st.subheader('b- Blood glucose level')
            st.write('You can notice that there are some outliers which are reasonable in the data.')
            st.plotly_chart(fy.fig9)
            st.plotly_chart(fy.fig10)

    
# Bivariate_analysis Tab

with tab_bivariate_analysis:
  # Title of tab
    option3 = st.radio('Choose the feature you want to review virsus the target (diabetes)', ('Age', 'Body mass index', 'HbA1c level', 'Blood glucose level', 'Gender', 'Hypertension', 'Heart disease', 'Smoking history', 'Correlation'))
    if option3 == 'Age':
        st.title('Bivariate Analysis') 
        st.subheader('1- Diabetes vs Age')
        st.write('You can notice that the probability of infection increases with age increasing')
        st.plotly_chart(fy.fig11)
        
    elif option3 == 'Body mass index':
        st.subheader('2- Diabetes vs Body mass index')
        st.write('You can notice that the probability of infection increases with bmi increasing')
        st.plotly_chart(fy.fig12)
        
    elif option3 == 'HbA1c level':
        st.subheader('3- Diabetes vs HbA1c level')
        st.write('You can notice that the probability of infection flipped at HbA1c_level = 6.8')
        st.plotly_chart(fy.fig13)
        
    elif option3 == 'Blood glucose level':
        st.subheader('4- Diabetes vs Blood glucose level')
        st.write('You can notice that the probability of infection flipped at blood_glucose_level = 220')
        st.plotly_chart(fy.fig14)
        
    elif option3 == 'Gender':
        st.subheader('5- Diabetes vs Gender')
        st.plotly_chart(fy.fig15)
        
    elif option3 == 'Hypertension':
        st.subheader('6- Diabetes vs Hypertension')
        st.plotly_chart(fy.fig16)
        
    elif option3 == 'Heart disease':
        st.subheader('7- Diabetes vs Heart disease')
        st.plotly_chart(fy.fig17)
        
    elif option3 == 'Smoking history':
        st.subheader('8- Diabetes vs Smoking history')
        st.plotly_chart(fy.fig18)

    else:
        st.subheader('9- Correlation')
        st.plotly_chart(fy.fig19)
