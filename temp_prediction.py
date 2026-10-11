import os, urllib.request, zipfile, io, pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
if not os.path.exists("beijing.csv"):
    data = urllib.request.urlopen("https://archive.ics.uci.edu/static/public/501/beijing+multi+site+air+quality+data.zip").read()
    inner = zipfile.ZipFile(io.BytesIO(zipfile.ZipFile(io.BytesIO(data)).open("PRSA2017_Data_20130301-20170228.zip").read()))
    with inner.open([f for f in inner.namelist() if f.endswith(".csv")][0]) as s, open("beijing.csv", "wb") as t:
        t.write(s.read())
df = pd.read_csv("beijing.csv").dropna(subset=["TEMP", "PM2.5", "PM10", "PRES", "DEWP", "WSPM"])
X = df[["PM2.5", "PM10", "PRES", "DEWP", "WSPM"]]
y = df["TEMP"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))
new_reading = pd.DataFrame([[80.0, 120.0, 1012.0, 12.0, 2.5]], columns=X.columns)
print("Predicted Temperature:", model.predict(new_reading)[0])
