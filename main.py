import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")

place = st.text_input("Place")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} day(s) in {place.title()}")

if place:
    try:
        data, date = get_data(place, days, option)

        if option == "Temperature":
            figure = px.line(x=date, y=data, labels={"x":"Date", "y":"Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear":"images/clear.png", "Clouds":"images/cloud.png",
                    "Rain":"images/rain.png", "Snow":"images/snow.png"}
            
            path = [images[condition] for condition in data]

            captions = []
            for i in range(len(data)):
                captions.append(data[i]+" , "+date[i])

            st.image(path, caption=captions, width=115)
        
    except KeyError:
        st.write("This place doesn't exist.")
    