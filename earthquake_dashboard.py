import streamlit as st
import requests
import pandas as pd
st.title("USGS Earthquake Analysis Dashboard")
url = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-08-07&endtime=2026-09-25&minmagnitude=2.5&orderby=time"
@st.cache_data
def load_data():
    res = requests.get(url).json()
    data = []
    for f in res["features"]:
        p = f["properties"]
        c = f["geometry"]["coordinates"]
        data.append({"Magnitude": p["mag"], "Place": p["place"], "Time": pd.to_datetime(p["time"], unit="ms"), "Longitude": c[0], "Latitude": c[1], "Depth": c[2], "Tsunami": p["tsunami"]})
    return pd.DataFrame(data)
df = load_data()
st.subheader("Raw Earthquake Data")
st.dataframe(df)
st.subheader("Statistical Analysis")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Events", len(df))
col2.metric("Max Magnitude", df["Magnitude"].max())
col3.metric("Avg Depth (km)", round(df["Depth"].mean(), 2))
col4.metric("Tsunami Warnings", int((df["Tsunami"] == 1).sum()))
st.write(df[["Magnitude", "Depth"]].describe())
st.subheader("Time-Series Analysis (Magnitude over Time)")
st.line_chart(df.set_index("Time")["Magnitude"])
st.subheader("Daily Earthquake Frequency")
daily = df.set_index("Time").resample("D").size()
st.bar_chart(daily)
st.subheader("Geographical Distribution")
st.map(df.rename(columns={"Latitude": "latitude", "Longitude": "longitude"}))
st.subheader("Key Findings")
st.write(f"1. Total earthquakes recorded (magnitude >= 2.5): {len(df)}")
st.write(f"2. Highest magnitude recorded: {df['Magnitude'].max()}")
st.write(f"3. Average earthquake depth: {round(df['Depth'].mean(), 2)} km")
st.write(f"4. Total tsunami alerts triggered: {int((df['Tsunami'] == 1).sum())}")
