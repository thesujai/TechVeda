import streamlit as st
from data.symptoms import symptoms
from result import result

def SymptomSelection():
    # st.title("Symptom Checker")
    # st.write("Select 5 symptoms and click 'Submit' to process and display the output.")

    col1, col2 = st.columns(2)
    with col1:
        symptom1 = st.selectbox("Symptom 1", ["Select a Symptom"]+symptoms)
    with col2:
        symptom2 = st.selectbox("Symptom 2", ["Select a Symptom"]+symptoms)
    
    col3, col4 = st.columns(2)
    with col3:
        symptom3 = st.selectbox("Symptom 3", ["Select a Symptom"]+symptoms)
    with col4:
        symptom4 = st.selectbox("Symptom 4", ["Select a Symptom"]+symptoms)
    symptom5 = st.selectbox("Symptom 5", ["Select a Symptom"]+symptoms)
    
    if st.button("Submit"):
        # model integration
        # 
        data={'disease':st.markdown("[Cancer](https://www.google.com)"),
              'treatment':{
                  'chemo':'adasdasd',
                  'a':'fewfewfew',
              }
              }
        result(data)
