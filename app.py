# -*- coding: utf-8 -*-
"""
Created on Sun May  8 21:01:15 2022

@author: Madhukesh Singh
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

import streamlit as st

# Add custom CSS for dark theme
st.markdown(
    """
    <style>
        body {
            background-color: #121212; /* Set dark background color */
            color: #fff; /* Set light text color */
        }
        
        .stApp {
            max-width: 1200px; /* Set max-width for the app */
        }

        .sidebar .sidebar-content {
            background-color: #212121; /* Set dark sidebar background color */
        }

        .main .block-container {
            background-color: #212121; /* Set dark main content background color */
        }

        /* Add more custom styling as needed */
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar for navigation
with st.sidebar:
    selected = st.selectbox(
        'Select Disease Prediction',
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction']
    )

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    
    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    # Add more input fields as needed

    # Code for Prediction
    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure]])
        diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'

    st.success(diab_diagnosis)

# Add similar sections for Heart Disease and Parkinson's Prediction
# ...

# Display the app
st.set_page_config(
    page_title='Disease Prediction App',
    page_icon=':heart:',
    layout='wide'
)














