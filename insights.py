def generate_insights(features, chapter_difficulty):
    insights = []

    # 1. High-risk students
    high_risk_students = features[
        features["early_risk_flag"] == 1
    ]["student_id"].tolist()

    insights.append(
        f"{len(high_risk_students)} students are identified as high risk and may drop out without intervention."
    )

    # 2. Completion statistics
    total_students = len(features)
    likely_complete = features[
        features["completion_prediction"] == 1
    ].shape[0]

    completion_rate = (likely_complete / total_students) * 100

    insights.append(
        f"Approximately {completion_rate:.1f}% of students are likely to complete the course."
    )

    # 3. Key factors affecting completion
    insights.append(
        "Low average assessment scores and reduced engagement time are the strongest indicators of dropout risk."
    )

    # 4. Chapter needing improvement
    most_difficult = chapter_difficulty.iloc[0]

    insights.append(
        f"Chapter {int(most_difficult['chapter_order'])} shows the highest difficulty and requires content or instructional improvement."
    )

    return {
        "high_risk_students": high_risk_students,
        "summary_insights": insights
    }
