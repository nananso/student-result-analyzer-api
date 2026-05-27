import pandas as pd

def assign_grade(avg):
    if avg >= 70:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "F"

def process_student_data(df):
    df["average"] = df[
        ["math", "english", "physics"]
    ].mean(axis=1)

    df["grade"] = df["average"].apply(assign_grade)

    return df