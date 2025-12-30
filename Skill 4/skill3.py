from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import joblib

df = pd.read_json('user_raw_data.json')

# print(df.head())

X = df[['monthly_usage', 'complaints', 'tenure']]
y = df['churned']

model = RandomForestClassifier()
model.fit(X, y)

# Here we are saving the model
joblib.dump(model, "churn_model.pkl")

# Here we are loading the data at runtime to pass this in pipelines
model = joblib.load("churn_model.pkl")

# Context creation (State Maintain)
class AutomationContext:
    def __init__(self, raw_data):
        self.raw_data = raw_data
        self.features = None
        self.decision = None
        self.action_status = None


# Building one feature to showcase
def build_features(context):
    u = context.raw_data

    context.features = [
        u["monthly_usage"],
        u["complaints"],
        u["tenure"]
    ]

    return context


# Decision making (AI)
def decision_engine(context, model):
    X = pd.DataFrame(
        [context.features],
        columns=["monthly_usage", "complaints", "tenure"]
    )

    prob = model.predict_proba(X)[0][1]

    if prob > 0.7:
        context.decision = "OFFER_DISCOUNT"
    elif prob > 0.4:
        context.decision = "SEND_WARNING"
    else:
        context.decision = "NO_ACTION"

    return context


# Action Engine
def action_engine(context):
    uid = context.raw_data["user_id"]

    if context.decision == "OFFER_DISCOUNT":
        print(f"Discount sent to user {uid}")
        context.action_status = "DONE"

    elif context.decision == "SEND_WARNING":
        print(f"Warning sent to user {uid}")
        context.action_status = "DONE"

    else:
        context.action_status = "SKIPPED"

    return context


# Pipeline (Sequential flow)
def automation_pipeline(raw_user_data, model):
    context = AutomationContext(raw_user_data)

    context = build_features(context)
    context = decision_engine(context, model)
    context = action_engine(context)

    return context


users = [
    {"user_id": 101, "monthly_usage": 35, "complaints": 4, "tenure": 3},
    {"user_id": 102, "monthly_usage": 120, "complaints": 0, "tenure": 12}
]

for user in users:
    result = automation_pipeline(user, model)
    print(result.decision)

"""
DATA SOURCE
   ↓
RAW USER DATA
   ↓
AUTOMATION PIPELINE
   ↓
MODEL (already trained & loaded)
   ↓
DECISION + ACTION
   ↓
LOG / STORE / MONITOR
"""