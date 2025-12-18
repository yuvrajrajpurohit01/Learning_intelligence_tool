import streamlit as st
import pandas as pd

from data_loader import load_data
from feature_engineering import create_features
from inference import load_model, predict_completion, detect_early_risk
from chapter_difficulty import calculate_chapter_difficulty
from insights import generate_insights


st.set_page_config(
    page_title="Learning Intelligence Tool",
    layout="wide"
)

st.title("📘 AI-Powered Learning Intelligence Tool")
st.write("Upload learner data to get predictions and insights.")

# File upload
uploaded_file = st.file_uploader(
    "Upload CSV file",
    type=["csv"]
)

if uploaded_file is not None:
    # Save uploaded file temporarily
    df = pd.read_csv(uploaded_file)

    st.subheader("📊 Raw Input Data")
    st.dataframe(df)

    # Feature engineering
    features = create_features(df)

    # Load model & predict
    model = load_model()
    features["completion_prediction"] = predict_completion(features, model)

    # Early risk detection
    features["early_risk_flag"] = detect_early_risk(features)

    # Chapter difficulty
    chapter_difficulty = calculate_chapter_difficulty(df)

    # Insights
    insights = generate_insights(features, chapter_difficulty)

    # -------------------------
    # Display Results
    # -------------------------

    st.subheader("🎓 Course Completion Predictions")
    st.dataframe(features)

    st.subheader("⚠️ High-Risk Students")
    st.write(insights["high_risk_students"])

    st.subheader("📘 Chapter Difficulty Analysis")
    st.dataframe(chapter_difficulty)

    st.subheader("💡 Key Insights")
    for insight in insights["summary_insights"]:
        st.write("•", insight)

else:
    st.info("Please upload a CSV file to begin analysis.")
