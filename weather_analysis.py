import requests
import pandas as pd
import matplotlib.pyplot as plt
url = "https://api.open-meteo.com/v1/forecast?latitude=9.93&longitude=76.27&current=temperature_2m,relative_humidity_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m"
res = requests.get(url).json()
df = pd.DataFrame(res["hourly"]).head(24)
print(df[["temperature_2m", "relative_humidity_2m"]].describe())
plt.subplot(2, 1, 1)
plt.bar(df["time"].str[-5:], df["temperature_2m"], color="orange")
plt.title("Temperature Trend (°C)")
plt.xticks(rotation=45)
plt.subplot(2, 1, 2)
plt.bar(df["time"].str[-5:], df["relative_humidity_2m"], color="blue")
plt.title("Humidity Trend (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
