import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
from preprocess import preprocess
from features import add_features

os.makedirs("models", exist_ok=True)

df = pd.read_csv("data/raw_data.csv")
df = preprocess(df)
df = add_features(df)

X = df[["salary_per_age"]]
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y)

model = LogisticRegression()
model.fit(X_train, y_train)

pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, pred))

joblib.dump(model, "models/model.joblib")
