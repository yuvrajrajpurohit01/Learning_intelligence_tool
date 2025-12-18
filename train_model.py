import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
import os

# Load dataset
df = pd.read_csv("sample_input.csv")

# Feature engineering
features = df.groupby("student_id").agg(
    avg_time_spent=("time_spent", "mean"),
    avg_score=("score", "mean"),
    chapters_completed=("completion_status", "sum"),
    total_chapters=("chapter_order", "count")
).reset_index()

# Target: course completion
features["will_complete"] = (
    features["chapters_completed"] >= features["total_chapters"]
).astype(int)

X = features[["avg_time_spent", "avg_score", "chapters_completed"]]
y = features["will_complete"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate
preds = model.predict(X_test)
print("Model Accuracy:", accuracy_score(y_test, preds))

# Save model
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/completion_model.pkl")

print(" Model trained and saved successfully")
