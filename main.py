import argparse
import json

from data_loader import load_data
from feature_engineering import create_features
from inference import (
    load_model,
    predict_completion,
    detect_early_risk
)
from chapter_difficulty import calculate_chapter_difficulty
from insights import generate_insights


def main():
    # CLI Argument Parsing
    parser = argparse.ArgumentParser(
        description="AI-powered Learning Intelligence Tool"
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Path to input CSV file"
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Path to output JSON report"
    )
    args = parser.parse_args()

    #1. Load Data
    df = load_data(args.input)

    # 2. Feature Engineering
    features = create_features(df)

    # 3. Course Completion Prediction
    model = load_model()
    completion_predictions = predict_completion(features, model)
    features["completion_prediction"] = completion_predictions

    # 4. Early Risk Detection
    early_risk_flags = detect_early_risk(features)
    features["early_risk_flag"] = early_risk_flags

    # 5. Chapter Difficulty Detection
    chapter_difficulty = calculate_chapter_difficulty(df)

    # 6. Insight Generation
    insights = generate_insights(features, chapter_difficulty)

    # 7. Final Output
    result = {
        "course_completion_predictions": features.to_dict(orient="records"),
        "chapter_difficulty_analysis": chapter_difficulty.to_dict(orient="records"),
        "insights": insights
    }

    with open(args.output, "w") as f:
        json.dump(result, f, indent=4)

    print("Learning Intelligence AI Tool executed successfully")


if __name__ == "__main__":
    main()
