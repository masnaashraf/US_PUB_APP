import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import image
from PIL import Image
import os


#Load data
df = pd.read_csv('clean_open_pubs.csv')

image = Image.open('image-1.jpg')
st.image(image)



st.title(":red[Location of all Pubs in UK 🍻🍻]")


location_type = st.selectbox(
    "Select the location type:",
    ('Postal Code', 'Local Authority'))

if location_type == 'Postal Code':
    location_options = df['postcode'].unique()
    location = st.selectbox("Select the Postal Code:", location_options)
    filtered_df = df[df['postcode'] == location]
    st.text("Details of  Pubs based on  the Postal Code:")
elif location_type == 'Local Authority':
    location_options = df['local_authority'].unique()
    location = st.selectbox("Select the Local Authority:", location_options)
    filtered_df = df[df['local_authority'] == location]
    st.text("Details of  Pubs based on local authority is:")
    

button_1 = st.button("Submit")

if button_1:
    st.text("Total Number of Pub:")
    st.text(filtered_df.shape[0])
    st.map(filtered_df)
    st.dataframe(filtered_df)
