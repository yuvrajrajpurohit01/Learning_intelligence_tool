import pandas as pd

def create_features(df):
    features = df.groupby("student_id").agg(
        avg_time_spent=("time_spent", "mean"),
        avg_score=("score", "mean"),
        chapters_completed=("completion_status", "sum")
    ).reset_index()

    return features
