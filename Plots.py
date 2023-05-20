#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 20 18:22:54 2023

@author: kiranchandra
"""

import numpy as np
import pandas as pd
import seaborn as sns #Data Visualisation Library
import streamlit as st 
import matplotlib.pyplot as plt

st.title("Plots")

st.header("1.0 Data Visualisation with StreamLit")

st.subheader('1.1 Generating and Loading the Random data')
chart_data = pd.DataFrame(np.random.randn(20,3), columns=['Line 1', 'Line 2', 'Line 3'])
st.write(chart_data)

st.subheader('1.2 Line Chart')
st.line_chart(chart_data)

st.subheader('1.3 Area Chart')
st.area_chart(chart_data)

st.subheader('1.4 Bar Chart')
st.bar_chart(chart_data)

st.header('2.0 Data Visualization with Matplotlib and Seaborn')


st.subheader('2.1 Loading the DataFrame')
df = pd.read_csv('Ref/Iris.csv')
st.dataframe(df)

st.subheader('2.2 Distribution Plot - Matplotlib')
fig = plt.figure(figsize=(15,8))
df['Species'].value_counts().plot(kind = 'bar')
st.pyplot(fig)

st.subheader('2.3 Distribution Plot - Seaborn')
fig = plt.figure(figsize= (15,8))
sns.distplot(df['SepalLengthCm'])
st.pyplot(fig)

st.header("3.0 Multiple Graphs in one columns")
col1, col2 = st.columns(2)
with col1:
    col1.header = 'KDE = False'
    fig1 = plt.figure(figsize=(5,5))
    sns.distplot(df['SepalLengthCm'], kde = False)
    st.pyplot(fig1)
with col2:
    col2.header = 'Hist = False'
    fig2 = plt.figure(figsize=(6,6))
    sns.distplot(df['SepalLengthCm'], hist = False)
    st.pyplot(fig2)
    
st.header('4.0 Changing Style')
col1, col2 = st.columns(2)
with col1:
    fig = plt.figure()
    sns.set_style('darkgrid')
    sns.set_context('notebook')
    sns.distplot(df['PetalLengthCm'], hist = False)
    st.pyplot(fig)
with col2:
    fig3 = plt.figure()
    sns.set_theme(context = 'poster' , style='darkgrid')
    sns.distplot(df['PetalLengthCm'], hist = False)
    st.pyplot(fig3)
    
st.header('5.0 Exploring different Graphs')

st.subheader('5.1 Scatter Plot')
fig,ax = plt.subplots(figsize = (15,8))
ax.scatter(*np.random.random(size = (2,100)))
st.pyplot(fig)

st.subheader('5.2 Count Plot')
fig = plt.figure(figsize=(15,8))
sns.countplot(data = df, x = 'Species')
st.pyplot(fig)

st.subheader('5.3 Box-Plot')
fig = plt.figure(figsize=(15,8))
sns.boxplot(data=df, x = 'Species', y='PetalLengthCm')
st.pyplot(fig)

st.subheader('5.4 Violin-Plot')
fig = plt.figure(figsize=(15,8))
sns.violinplot(data=df, x = 'Species', y='PetalLengthCm')
st.pyplot(fig)
    
