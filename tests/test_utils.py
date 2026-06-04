import pandas as pd
from app.utils import assign_grade, process_student_data


def test_assign_grade_A():
    assert assign_grade(85) == "A"


def test_assign_grade_B():
    assert assign_grade(65) == "B"


def test_assign_grade_C():
    assert assign_grade(55) == "C"


def test_assign_grade_F():
    assert assign_grade(30) == "F"


def test_process_student_data():
    df = pd.DataFrame({
        "name": ["John"],
        "math": [80],
        "english": [70],
        "physics": [90]
    })

    result = process_student_data(df)

    assert "average" in result.columns
    assert "grade" in result.columns
    assert result["grade"][0] == "A"