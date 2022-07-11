import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import unicodedata


data = pd.read_csv("oai_setnames.csv", encoding = "utf-8")
data = data.drop(["Unnamed: 0.1", "Unnamed: 0"], axis=1)
main = data.["Main"].drop_duplicates()

          


dnbcolor = ['#FEFEFE', '#2499ff', '#f33930', '#b6c73f', '#ffd44d',
            '#3cb8f6', '#f9852e', '#e3d98f', '#000000', '#01be00']
testcolor = ['#ff6900', '#fcb900', '#7bdcb5', '#00d084', '#8ed1fc',
            '#0693e3', '#abb8c3', '#eb144c', '#f78da7', '#9900ef']


st.header('Übersicht OAI-Sets der DNB')

st.write("Hier finden Sie eine Übersicht der über die OAI-Schnittstelle zur Verfügung stehenden Sets: ") 

mychoice = st.selectionsbox("Auswahl:", main)


choice = st.selectbox(
            "Folgende übergeordnete OAI-Sets stehen zur Verfügung:", 
            ('Deutsche Nationalbibliografie (DNB)', 
             'Deutsche Nationalbibliografie (DNB) - APPR',
             'Deutsche Nationalbibliografie: Monografien und Periodika des Verlagsbuchhandels',
             'Deutsche Nationalbibliografie: Monografien und Periodika außerhalb des Verlagsbuchhandels',
             'Deutsche Nationalbibliografie: Karten', 
             'Deutsche Nationalbibliografie: Hochschulschriften',
             'Deutsche Nationalbibliografie: Musikalien',
             'Deutsche Nationalbibliografie: Online-Publikationen',
             'Deutsche Nationalbibliografie: Musiktonträger',
             'Deutsche Nationalbibliografie: Kataloganreicherung (TOC-Service)',
             'Deutsche Nationalbibliografie (nur Datensaetze nach abgeschlossener Bearbeitung)',
             'Deutsche Nationalbibliografie (nur Datensaetze nach abgeschlossener Bearbeitung): Publikationen des Verlagsbuchhandels',
             'Deutsche Nationalbibliografie (nur Datensaetze nach abgeschlossener Bearbeitung): Publikationen ausserhalb des Verlagsbuchhandels',
             'Deutsche Nationalbibliografie (nur Datensaetze nach abgeschlossener Bearbeitung): Karten',
             'Deutsche Nationalbibliografie (nur Datensaetze nach abgeschlossener Bearbeitung): Hochschulschriften',
             'Deutsche Nationalbibliografie (nur Datensaetze nach abgeschlossener Bearbeitung): Musikalien',
             'Deutsche Nationalbibliografie (nur Datensaetze nach abgeschlossener Bearbeitung): Online-Publikationen',
             'Deutsche Nationalbibliografie: Monografien und Periodika des Verlagsbuchhandels - APPR',          
            ))

st.write("Stand der Daten: 22.03.2022")

st.dataframe(data)


#Jahre: 
#data = data[data['Year'].notna()]
#data = data.astype({'Year':'int'})
#data = data[(data['Year'] >= 1900) & (data['Year'] <= 2100)]

#s = data['Year'].value_counts()[:33].sort_index()
#fig = px.bar(s, labels={'index':'Jahr', 'value':'Anzahl'}, color='value', height=500)
#st.plotly_chart(fig, use_container_width=True)

#st.info("INFO: Es werden die Daten für die Jahre 1990 bis 2022 (laufend) dargestellt. " ) 
