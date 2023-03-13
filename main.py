import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Select Number of days", min_value=1, max_value=5,
                 help="Select the number of days to forecast the weather")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for next {days} days in {place} is: ")


# Get the temperature/sky data
if place:
    try:
        filtered_data = get_data(place, days)
        if option == "Temperature":
            temperatures = [dict["main"]["temp"] - 273.15 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            # Create a temp plot
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature(C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
            images = {"Clouds": "images/cloud.png",
                      "Rain": "images/rain.png",
                      "Clear":"images/clear.png",
                      "Snow":"images/snow.png"}
            images_path = [images[condition] for condition in filtered_data]
            st.image(images_path, width=115)
    except KeyError:
        st.info("Type a correct place!")
