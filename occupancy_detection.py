import os, requests, zipfile, io, pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
if not os.path.exists("datatraining.txt"):
    r = requests.get("https://archive.ics.uci.edu/static/public/357/occupancy+detection.zip")
    zipfile.ZipFile(io.BytesIO(r.content)).extract("datatraining.txt")
df = pd.read_csv("datatraining.txt")
X = df[["Temperature", "Humidity", "Light", "CO2"]]
y = df["Occupancy"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Accuracy Score:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))