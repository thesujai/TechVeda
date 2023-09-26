import streamlit as st
import pandas as pd

# data = pd.read_csv("/path")

st.title("Cure Prediction")

nav = st.sidebar.radio("Navigation",["Home","Prediction"])
if nav == "Home":
  st.image("data//img//homepage.jpeg",width = 600)
  st.subheader("Project Description")
  st.write("The goal of the project is to create a predictive model or system that takes a set of symptoms as input and then uses machine learning algorithms to recommend Ayurvedic remedies or treatments that are most suitable for the identified disease or health condition.")

if nav == "Prediction":
  st.write("Predict")