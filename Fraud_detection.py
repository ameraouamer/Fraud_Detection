import joblib
import pandas as pd
import streamlit as st  


model = joblib.load('fraud_detection_model.pkl')

st.title('Fraud Detection Model')
st.markdown('please enter the transaction details and use use the predict button ')
st.divider(