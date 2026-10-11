import streamlit as st
import requests
import pandas as pd
st.title("Kochi Air Quality Dashboard")
url = "https://air-quality-api.open-meteo.com/v1/air-quality?latitude=9.93&longitude=76.27&hourly=pm10,pm2_5,us_aqi&timezone=auto"
@st.cache_data
def get_data():
    res = requests.get(url).json()
    df = pd.DataFrame(res["hourly"])
    df["time"] = pd.to_datetime(df["time"])
    return df
df = get_data()
st.subheader("Statistical Analysis")
col1, col2, col3 = st.columns(3)
col1.metric("Avg US AQI", round(df["us_aqi"].mean(), 2))
col2.metric("Max PM2.5 (µg/m³)", df["pm2_5"].max())
col3.metric("Max PM10 (µg/m³)", df["pm10"].max())
st.write(df[["us_aqi", "pm2_5", "pm10"]].describe())
st.subheader("Time-Series Analysis: AQI Over Time")
st.line_chart(df.set_index("time")["us_aqi"])
st.subheader("Time-Series Analysis: PM2.5 & PM10 Levels Over Time")
st.line_chart(df.set_index("time")[["pm2_5", "pm10"]])
st.subheader("Hourly Air Quality Data")
st.dataframe(df)
