import streamlit as st
import requests

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

st.markdown('''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
''')

# Input controls
pickup_datetime = st.text_input("Date and time", "2014-07-06 19:18:00")
pickup_longitude = st.number_input("Pickup longitude", value=-73.950655)
pickup_latitude = st.number_input("Pickup latitude", value=40.783282)
dropoff_longitude = st.number_input("Dropoff longitude", value=-73.984365)
dropoff_latitude = st.number_input("Dropoff latitude", value=40.769802)
passenger_count = st.number_input("Passenger count", min_value=1, max_value=8, value=1)

# API endpoint (tu URL real)
url = 'https://taxifare-825042233153.europe-west1.run.app/predict'

if st.button("Predict fare"):
    # Armar el diccionario con los parámetros
    params = {
        "pickup_datetime": pickup_datetime,
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count
    }

    # Hacer el request
    response = requests.get(url, params=params)

    if response.status_code == 200:
        prediction = response.json().get("fare", "N/A")
        st.success(f"Estimated fare: ${prediction:.2f}")
    else:
        st.error("Something went wrong. Please check your input and try again.")
