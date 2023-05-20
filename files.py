#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 20 18:07:05 2023

@author: kiranchandra
"""

import streamlit as st
import pandas as pd

st.title("Files Loader")
st.subheader('Uploading the csv/xlsx File.')
df = st.file_uploader("Upload the csv file : ", type=['csv', 'xlsx'])




if df is not None:
    fileType = str(df.name).split('.')
    if fileType[1] == 'csv':
        st.subheader('Loading the CSV File.')
        dataFrame = pd.read_csv('Ref'+'/'+str(df.name))
        st.table(dataFrame.head())
    else:
        st.subheader('Loading the Excel File.')
        dataFrame = pd.read_excel('Ref'+'/'+str(df.name))
        st.table(dataFrame.head())
        

st.subheader('Dealing with the Images')

# st.write('Displaying static image :')
# st.image('Ref/kc.jpg')

img = st.file_uploader("Upload the Image file : ", type=['jpg','jpef','gif','png'])

if img is not None:
    st.write('Displaying the uploaded Image :')
    st.image(img)
    
st.subheader("Working with Video Files")
videoFile = st.file_uploader("Upload the video file :", type=['mkv', 'mp4'])
if videoFile is not None:
    st.video(videoFile, start_time=0)
    
st.subheader("Working with Audio Files")
audioFile = st.file_uploader("Upload the audio file :", type=['mp3', 'wav'])
if audioFile is not None:
    st.audio(audioFile.read(), start_time=0)