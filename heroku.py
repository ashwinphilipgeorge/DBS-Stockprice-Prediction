import streamlit as st
import joblib
import pandas as pd
import numpy as np

st.title('DBS Share Predictor')
model = joblib.load("./dbs_linear_model")

@st.cache
def load_data():
    data = pd.read_csv("./dbs_singdollar.csv")
    data.drop('Unnamed: 0',axis=1,inplace=True)
    return data

st.subheader("View Dataset here")
data_load_state = st.text('Loading data...')
data = load_data()
data_load_state.text("Data has been loaded! Click the checkbox to see the data example.")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

if st.checkbox('Show graph analysis'):
    dbs_chart_data = data.drop(['Date','SGD'],axis=1)
    sgd_chart_data = data.drop(['Date','DBS'],axis=1)
    st.subheader('DBS Stock Prices with time')
    st.line_chart(data=dbs_chart_data, use_container_width=True)
    st.subheader ('SGD value against the USD with time')
    st.line_chart(data=sgd_chart_data, use_container_width=True)



st.subheader("Predict the DBS shareprice here!")
dbs_value = st.text_input('What is the value of the Singapore Dollar ($1USD) you want to predict at?')


def predictor(model,value):
    prediction = model.predict([[value]])
    return prediction

value = predictor(model,dbs_value)
st.write('The DBS Shareprice is expected to be: $' + str(round(value[0][0],2)) + ' at this SGD value')
    

    