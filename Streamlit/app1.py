
import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st
import os
os.system('sudo pip install scikit-learn')

from PIL import Image
def welcome():
    return "Welcome All"

def predict_note_authentication(IsHoliday, Temperature, Fuel_Price, Size, day, year,
       month, mean, std, skew, kurtosis, Type_B, Type_C):
    
    """Let's Authenticate the Weekly Sales
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: IsHoliday
        in: query
        type: number
        required: true
      - name: Temperature
        in: query
        type: number
        required: true      
	- name: Fuel_Price
        in: query
        type: number
        required: true      
	- name: Size
        in: query
        type: number
        required: true      	
	- name: day
        in: query
        type: number
        required: true      	
	- name: year
        in: query
        type: number
        required: true
	- name: month
        in: query
        type: number
        required: true
	- name: mean
        in: query
        type: number
        required: true
      - name: std
        in: query
        type: number
        required: true
      - name: skew
        in: query
        type: number
        required: true
      - name: kurtosis
        in: query
        type: number
        required: true
      - name: Type_B
        in: query
        type: number
        required: true
      - name: Type_C
        in: query
        type: number
        required: true

    responses:
        200:
            description: The output values
        
    """
    loaded_model = pickle.load(open(r'C:\Users\LENOVO\OneDrive\Desktop\Streamlit\DTR_pickle_v2','rb'))
    prediction=loaded_model.predict([[IsHoliday, Temperature, Fuel_Price, Size, day, year,
       month, mean, std, skew, kurtosis, Type_B, Type_C]])
    print(prediction)
    return prediction

def main():
    st.title("weekly sales")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Weekly Sales ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    IsHoliday = st.text_input("IsHoliday","Enter 1 for Not Holiday")
    Temperature= st.text_input("Temperature","Type Here")
    Fuel_Price= st.text_input("Fuel_Price","Type Here")
    Size= st.text_input("Size","Type Here")
    day = st.text_input("day","Type Here")
    year= st.text_input("year","Type Here")
    month = st.text_input("month","Type Here")
    mean = st.text_input("mean","Type Here")
    std = st.text_input("std","Type Here")
    skew = st.text_input("skew","Type Here")
    kurtosis = st.text_input("kurtosis","Type Here")
    Type_B= st.text_input("Type_B","Type Here")
    Type_C= st.text_input(" Type_C","Type Here")


    result=""
    if st.button("Predict Weekly Sales"):
        result=predict_note_authentication(IsHoliday, Temperature, Fuel_Price, Size, day, year,
       month, mean, std, skew, kurtosis, Type_B, Type_C)
    st.success('The Weekly forecasted Sales is {}'.format(result))
    if st.button("About"):
        st.text("App built by Team 6")
        st.text(""" 
                    1.Abhishek
                    2.Sumeet
                    3.Vaibhav
                    4.Hrishikesh and 
                    5.Vedant
                    """)

if __name__=='__main__':
    main()