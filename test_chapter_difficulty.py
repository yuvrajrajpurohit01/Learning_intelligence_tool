import pandas as pd
from chapter_difficulty import calculate_chapter_difficulty

def test_chapter_difficulty_not_empty():
    df = pd.DataFrame({
        "student_id": [1,1,2,2],
        "chapter_order": [1,2,1,2],
        "time_spent": [30,60,25,55],
        "score": [70,50,75,45],
        "completion_status": [1,0,1,0]
    })

    chapter_df = calculate_chapter_difficulty(df)

    assert not chapter_df.empty
    assert "difficulty_score" in chapter_df.columns
