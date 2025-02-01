import streamlit as st
import pydeck as pdk

# Streamlit app title
st.title("Where is Aidan Now?")

# Default location (can be changed by user)
default_lat = 49.2827  # Vancouver, BC
default_lon = -123.1207

# User input for location
latitude = st.number_input("Enter Latitude", value=default_lat, format="%f")
longitude = st.number_input("Enter Longitude", value=default_lon, format="%f")

# Define the location as a Pydeck Layer
layer = pdk.Layer(
    "ScatterplotLayer",
    data=[{"lat": latitude, "lon": longitude}],
    get_position="[lon, lat]",
    get_color="[255, 0, 0, 160]",
    get_radius=500000,
)

# Set the map view
view_state = pdk.ViewState(latitude=latitude, longitude=longitude, zoom=3, pitch=0)

# Render the map
st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))

st.write(f"### Current Location: ({latitude}, {longitude})")
