import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.write('# NO!!!! I WAS AT PEACE')


df = pd.read_csv("data\Austin_Animal_Center_Intakes-091922.csv")


intake = st.radio(label='What Intake Type?', options=df['Intake Type'].unique())


segment_df = df.loc[df['Intake Type'] == intake]

type_counts = segment_df['Animal Type'].value_counts(normalize=True)

col1, col2 = st.columns(2)

with col1:
    st.write('## Type Counts')
    st.write(type_counts)

# fig, ax = plt.subplots()

# ax.bar(x=type_counts.index, height=type_counts.values)

# st.write(fig)



with col2:
    st.write('## Streamlit Bar')
    st.bar_chart(type_counts)
