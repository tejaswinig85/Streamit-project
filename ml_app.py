import streamlit as st
import joblib
import os
import pandas as pd
import numpy as np
import pickle

# Attribute Information
attrib_info = """
Attribute Information:
Fixed acidity;
Volatile acidity;
Citric acid;
Residual sugar;
Chlorides;
Free sulfur dioxide;
Total sulfur dioxide;
Density;
pH;
Sulphates;
Alcohol;
Quality.
"""

# Replace function
def get_fvalue(val):
    feature_dict = {"No": 0, "Yes": 1}
    for key, value in feature_dict.items():
        if val == key:
            return value

def load_model(model_file):
    loaded_model = joblib.load(open(os.path.join(model_file), "rb"))
    return loaded_model

# Main ML App Function
def run_ml_app():
    st.header("ML")

    submenu = ["Logistic Regression", "Decision Tree"]
    st.sidebar.selectbox("submenu", submenu)
    st.subheader("ML Prediction")

    with st.expander("Attribute Info"):
        st.write(attrib_info)

    # Layout
    col1, col2 = st.columns(2)

    with col1:
        fixed_acidity = st.number_input("Fixed Acidity", value=7.4, step=0.1)
        volatile_acidity = st.number_input("Volatile Acidity", value=0.70, step=0.01)
        citric_acid = st.number_input("Citric Acid", value=0.00, step=0.01)
        residual_sugar = st.number_input("Residual Sugar", value=1.9, step=0.1)
        chlorides = st.number_input("Chlorides", value=0.076, step=0.001)
        free_sulfur_dioxide = st.number_input("Free Sulfur Dioxide", value=11.0, step=1)
        total_sulfur_dioxide = st.number_input("Total Sulfur Dioxide", value=34.0, step=1)

    with col2:
        density = st.number_input("Density", value=0.9978, step=0.0001)
        pH = st.number_input("pH", value=3.51, step=0.01)
        sulphates = st.number_input("Sulphates", value=0.56, step=0.01)
        alcohol = st.number_input("Alcohol", value=9.4, step=0.1)
        quality = st.number_input("Quality", value=5, step=1)

    with st.expander("Your Selected Options"):
        result = {
            'fixed acidity': fixed_acidity,
            'volatile acidity': volatile_acidity,
            'citric acid': citric_acid,
            'residual sugar': residual_sugar,
            'chlorides': chlorides,
            'free sulfur dioxide': free_sulfur_dioxide,
            'total sulfur dioxide': total_sulfur_dioxide,
            'density': density,
            'pH': pH,
            'sulphates': sulphates,
            'alcohol': alcohol,
            'quality': quality
        }
        st.write(result)

        encoded_result = []
        for i in result.values():
            if isinstance(i, int):
                encoded_result.append(i)
            elif i in ['Male', 'Female']:
                res = get_value(i)
                encoded_result.append(res)
            else:
                res1 = get_fvalue(i)
                encoded_result.append(res1)
        st.write(encoded_result)

    with st.expander("Prediction Result"):
        single_sample = pd
        free_sulfur_dioxide = st.number_input("Free Sulfur Dioxide", value=11.0, step=0.1)

