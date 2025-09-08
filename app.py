import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time
import streamlit as st


df = pd.read_csv('bank.csv')
st.set_page_config(page_title="Real Time Analysis Dashboard", page_icon='✅', layout='wide')
st.title("Real Time Live Data Analysis Dashboard")

job_filter = st.selectbox("Select the Job Type", pd.unique(df['job']))
df=df[df['job']==job_filter]

avg_age = np.mean(df['age'])
count_married = int(df[(df['marital']=='married')]['marital'].count())
balance = np.mean(df['balance'])

kpi1, kpi2, kpi3 = st.columns(3)
kpi1.metric(label="Age ⌛", value= round(avg_age), delta=round(avg_age))
kpi2.metric(label="Married 💍", value= int(count_married), delta=round(count_married))
kpi3.metric(label="Balance 💰", value= f'$ {round(balance),2}', delta=round(balance/count_married) * 100)

col1, col2 = st.columns(2)
with col1:
    fig1 = plt.figure(figsize=(10,5))
    sns.barplot(data=df, y='age', x='marital',palette='muted')
    st.pyplot(fig1)

with col2:
    fig2 = plt.figure(figsize=(10,5))
    sns.histplot(data=df, x='age',kde=True)
    st.pyplot(fig2)
