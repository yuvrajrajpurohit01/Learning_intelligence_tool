import joblib
import os

MODEL_PATH = "models/completion_model.pkl"

def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError("Trained model not found")
    return joblib.load(MODEL_PATH)

def predict_completion(features, model):
    X = features[["avg_time_spent", "avg_score", "chapters_completed"]]
    return model.predict(X)


def detect_early_risk(features):
    risk_flags = []

    for _, row in features.iterrows():
        if (
            row["completion_prediction"] == 0 or
            row["avg_score"] < 50 or
            row["avg_time_spent"] < 25
        ):
            risk_flags.append(1)  # High risk
        else:
            risk_flags.append(0)  # Low risk

    return risk_flags
