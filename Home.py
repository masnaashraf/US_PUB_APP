import streamlit as st
import pandas as pd
from matplotlib import image
from PIL import Image
import os


st.title(":red[Open Pubs Application UK 🍻🍻]")


image = Image.open('image-1.jpg')
st.image(image)

df = pd.read_csv('clean_open_pubs.csv')

st.subheader(":blue[Information regarding the Dataset]")

st.markdown("## Top Five Rows of Dataset")
st.write(df.head())

st.markdown("## Total Numbers of Rows and Columns")
st.write("Total number of rows:", df.shape[0])
st.write("Total number of columns:", df.shape[1])

st.markdown("## Displaying statistical Information regarding the Dataset")
st.write(df.describe())

st.markdown("## Displaying the Data Types of each column")
st.write(df.dtypes)


