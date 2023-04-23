import streamlit as st
import pandas as pd
from matplotlib import image
from PIL import Image

st.title(":red[Find the Nearest Pub in UK 🍻🍻]")
image = Image.open('image-1.jpg')
st.image(image)


df = pd.read_csv('clean_open_pubs.csv')

lat=st.number_input(label="Enter Latitude Here", min_value=49.892485, max_value=60.764969)

longi=st.number_input(label="Enter Longitude Here", min_value=-7.384525, max_value=1.757763)

if st.button("Find nearest pubs"):
    if lat and longi:
        user_location = (float(lat), float(longi))
        df['distance'] = df.apply(lambda row: ((row['latitude'] - user_location[0])**2 + (row['longitude'] - user_location[1])**2)**0.5, axis=1)
        nearest_df = df.nsmallest(5, 'distance')

    #List of Bar Names
    st.subheader(f"Nearest five pubs for the Latitude and Longitube you entered:")

    #Show Nearest Pubs on Map
    #st.map(data=nearest_df, zoom=None, use_container_width=True)
    st.map(data=nearest_df)

        #Name and Address of Nearby Pubs
    st.table(nearest_df[['name','address','local_authority','latitude','longitude']])