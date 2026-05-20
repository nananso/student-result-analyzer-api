from fastapi import FastAPI
from app.utils import calculate_average

app = FastAPI(
    title="Student Result Analyzer",
    description="An API for analyzing student academic performance",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Student Result Analyzer API running successfully"
    }

@app.get("/average")
def average():
    scores = [70, 85, 90, 60]
    avg = calculate_average(scores)

    return {
        "scores": scores,
        "average": avg
    }