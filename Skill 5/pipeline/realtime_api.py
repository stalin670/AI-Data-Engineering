from fastapi import FastAPI
import joblib
from context import PipelineContext
from feature_builder import build_features

app = FastAPI()

model = joblib.load("../model/churn_model.pkl")

@app.post("/predict")
def predict(user: dict):

    context = PipelineContext(user)

    context = build_features(context)

    prob = model.predict_proba([context.features])[0][1]

    context.prediction = prob

    return {
        "user_id": user["user_id"],
        "churn_probability": round(prob, 3)
    }
