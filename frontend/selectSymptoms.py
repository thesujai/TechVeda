import streamlit as st
from data.symptoms import symptoms
from result import result

def SymptomSelection():
    # st.title("Symptom Checker")
    # st.write("Select 5 symptoms and click 'Submit' to process and display the output.")

    # Dropdown menus for symptoms
    symptom1 = st.selectbox("Symptom 1", ["Select a Symptom"]+symptoms)
    symptom2 = st.selectbox("Symptom 2", ["Select a Symptom"]+symptoms)
    symptom3 = st.selectbox("Symptom 3", ["Select a Symptom"]+symptoms)
    symptom4 = st.selectbox("Symptom 4", ["Select a Symptom"]+symptoms)
    symptom5 = st.selectbox("Symptom 5", ["Select a Symptom"]+symptoms)
    
    if st.button("Submit"):
        # model integration
        data={}
        result(data)
