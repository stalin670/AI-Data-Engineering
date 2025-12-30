import pandas as pd
import joblib
from context import PipelineContext
from feature_builder import build_features, FEATURE_COLUMNS

model = joblib.load("../model/churn_model.pkl")

df = pd.read_csv("../data/batch_input.csv", sep="\t")

results = []

for _, row in df.iterrows():

    context = PipelineContext(row)

    # Create model-ready DataFrame
    input_df = pd.DataFrame([row])[FEATURE_COLUMNS]

    prob = model.predict_proba(input_df)[0][1]

    context.prediction = prob

    results.append({
        "user_id": row["user_id"],
        "churn_probability": round(prob, 3)
    })

output_df = pd.DataFrame(results)
output_df.to_csv("../data/predictions_output.csv", index=False)

print("Batch inference complete!")
