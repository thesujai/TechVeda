import streamlit as st

def result(data):
    # st.write(data.disease)
    st.title("Disease Prediction and Treatment")
    for key,value in data.items():
        st.write(key,value)