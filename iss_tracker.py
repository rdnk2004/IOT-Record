import requests
import time
import pandas as pd
import matplotlib.pyplot as plt
url = "http://api.open-notify.org/iss-now.json"
records = []
while len(records) < 100:
    try:
        res = requests.get(url, timeout=5).json()
        lat = float(res["iss_position"]["latitude"])
        lon = float(res["iss_position"]["longitude"])
        records.append({"timestamp": res["timestamp"], "latitude": lat, "longitude": lon})
        print(f"Record {len(records)}/100: Lat={lat}, Lon={lon}")
        time.sleep(5)
    except Exception:
        time.sleep(2)
df = pd.DataFrame(records)
df.to_csv("iss_data.csv", index=False)
print(df[["latitude", "longitude"]].describe())
plt.subplot(2, 1, 1)
plt.plot(df["timestamp"], df["latitude"], color="red")
plt.title("Latitude vs Time")
plt.subplot(2, 1, 2)
plt.plot(df["timestamp"], df["longitude"], color="blue")
plt.title("Longitude vs Time")
plt.tight_layout()
plt.show()
