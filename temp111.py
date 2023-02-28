# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import pickle
import streamlit as st 
from sklearn.ensemble import RandomForestClassifier
from pickle import dump
from pickle import load

# Loading trained model and making predictions
rf_model = pickle.load(open(r"C:\Users\lenovo\Downloads\filenalized model", "rb"))

def welcome():
    return "Welcome all" 

def prediction_authentication(account_length,  voice_mail_messages, evening_mins,  international_mins, customer_service_calls,international_plan,day_calls,  evening_calls, evening_charge, night_charge,international_calls, international_charge, total_charge):    

    prediction=rf_model.predict([[account_length,  voice_mail_messages, evening_mins,  international_mins, customer_service_calls,international_plan,day_calls,  evening_calls, evening_charge, night_charge,international_calls, international_charge, total_charge]])
    print (prediction)
    if prediction==0:
        return "customer will not churn"
    else:
        return "customer will churn"
    return prediction


  
def main():
  st.title("Model Deployment: Telco Customer Churn prediction")
  
  
account_length = st.text_input("Enter the account length")
voice_mail_messages = st.text_input("Enter the number of voice mail messages")
evening_mins = st.text_input("Enter the evening mins")
international_mins = st.text_input("Enter the international mins")
customer_service_calls = st.text_input("Enter the customer_service calls")
international_plan = st.text_input("Enter the international plan")
day_calls = st.text_input("Enter the day calls")
evening_calls = st.text_input("Enter the evening calls")
evening_charge = st.text_input("Enter the evening charge")
night_charge = st.text_input("Enter the night charge")
international_calls = st.text_input("Enter the international calls")
international_charge = st.text_input("Enter the international charge")
total_charge = st.text_input("Enter the total charge")

result=""
if st.button('prediction'):
    result = prediction_authentication(account_length,voice_mail_messages, evening_mins, international_mins, customer_service_calls, international_plan, day_calls,  evening_calls, evening_charge, night_charge, international_calls, international_charge, total_charge)
st.success('The output is{}'.format(result))


if __name__=='__main__':
    main()