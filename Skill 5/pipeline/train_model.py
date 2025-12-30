import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
from feature_builder import FEATURE_COLUMNS

df = pd.read_csv("../data/training_data.csv", sep="\t")

# print("Imported FEATURE_COLUMNS =", FEATURE_COLUMNS)
# print("CSV Columns =", df.columns.tolist())


X = df[FEATURE_COLUMNS]
y = df["churned"]

model = RandomForestClassifier(n_estimators=200)
model.fit(X, y)

joblib.dump(model, "../model/churn_model.pkl")

print("Model trained & saved!")
