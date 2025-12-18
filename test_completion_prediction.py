import pandas as pd
from inference import detect_early_risk

def test_early_risk_flagging():
    df = pd.DataFrame({
        "student_id": [1, 2],
        "avg_time_spent": [10, 60],
        "avg_score": [30, 85],
        "chapters_completed": [1, 3],
        "completion_prediction": [0, 1]
    })

    risks = detect_early_risk(df)

    assert risks[0] == 1  # High risk
    assert risks[1] == 0  # Low risk
