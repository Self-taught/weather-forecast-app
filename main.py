import streamlit as st
import plotly.express as px
import get_data from backend.py

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Select Number of days", min_value=1, max_value=5,
                 help="Select the number of days to forecast the weather")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for next {days} days in {place} is: ")

data = get_data(place, days, option)
dates = ["2023-03-12", "2023-03-13", "2023-03-14"]
temperatures = [10, 11, 15]
figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature(C)"})

st.plotly_chart(figure)
