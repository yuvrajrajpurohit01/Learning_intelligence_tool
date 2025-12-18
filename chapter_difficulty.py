def calculate_chapter_difficulty(df):
    # Aggregate chapter-level statistics
    chapter_df = df.groupby("chapter_order").agg(
        total_students=("student_id", "count"),
        dropout_rate=("completion_status", lambda x: 1 - x.mean()),
        avg_score=("score", "mean"),
        avg_time_spent=("time_spent", "mean")
    ).reset_index()

    # Normalize components
    chapter_df["low_score_factor"] = 1 - (chapter_df["avg_score"] / 100)
    chapter_df["time_factor"] = (
        chapter_df["avg_time_spent"] / chapter_df["avg_time_spent"].max()
    )

    # Difficulty score
    chapter_df["difficulty_score"] = (
        chapter_df["dropout_rate"] * 0.5 +
        chapter_df["low_score_factor"] * 0.3 +
        chapter_df["time_factor"] * 0.2
    )

    # Sort by most difficult
    chapter_df = chapter_df.sort_values(
        by="difficulty_score", ascending=False
    )

    return chapter_df
