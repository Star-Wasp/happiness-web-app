import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv("happy.csv")

st.title("In Search For Happiness")

x = st.selectbox("Select X Axis", ("happiness", "generosity", "life_expectancy"))
y = st.selectbox("Select Y Axis", ("social_support", "freedom_to_make_life_choices", "gdp"))
st.subheader(f"{x.replace("_", " ")} and {y.replace("_", " ")}")


figure = px.scatter(
    x=df[x],
    y=df[y],
    labels={"x": x.replace("_", " ").upper(), "y": y.replace("_", " ").upper()}
)
st.plotly_chart(figure)

st.text("Note: There seems to be a correlation between happiness and social support. I find that interesting and very telling. I hope you enjoy this simple web app!")
st.text("-StarWasp7272")