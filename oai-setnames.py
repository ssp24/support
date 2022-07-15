import streamlit as st
import pandas as pd
import numpy as np


data = pd.read_csv("oai_setnames.csv", encoding = "utf-8")
data = data.drop(["Unnamed: 0.1", "Unnamed: 0"], axis=1)
main = data["Main"].drop_duplicates()

          
st.header('Übersicht OAI-Sets der DNB')

st.write("Hier finden Sie eine Übersicht der über die OAI-Schnittstelle zur Verfügung stehenden Sets: ") 


test = st.selectbox(
          "Folgende übergeordnete OAI-Sets stehen zur Verfügung:", 
          (main))


if test: 
          selection = data[["Second", "Set"]].loc[data["Main"] == test]
          st.dataframe(selection)
else:
          st.write("Es wurde noch keine Auswahl getätigt.")


st.write("Stand der Daten: 11.07.2022")

