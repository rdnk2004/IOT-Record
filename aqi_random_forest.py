import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
df = pd.read_csv("city_day.csv").dropna(subset=["AQI_Bucket", "PM2.5", "PM10", "NO2", "CO", "SO2", "O3"])
X = df[["PM2.5", "PM10", "NO2", "CO", "SO2", "O3"]]
y = df["AQI_Bucket"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Accuracy Score:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
new_reading = pd.DataFrame([[30.0, 55.0, 15.0, 0.5, 8.0, 20.0]], columns=X.columns)
print("Predicted Air Quality:", model.predict(new_reading)[0])
