# from fastapi import FastAPI, UploadFile, File
# import pandas as pd
# from app.utils import process_student_data

# app = FastAPI(
#     title="Student Result Analyzer",
#     description="API for analyzing student performance",
#     version="1.0.0"
# )

# @app.get("/")
# def home():
#     return {
#         "message": "Student Result Analyzer API running successfully"
#     }

# @app.post("/analyze")
# async def analyze_results(file: UploadFile = File(...)):
#     try:
#         df = pd.read_csv(file.file)

#         processed_df = process_student_data(df)

#         results = processed_df.to_dict(orient="records")

#         return {
#             "total_students": len(results),
#             "results": results
#         }

#     except Exception as e:
#         return {
#             "error": str(e)
#         }


from fastapi import FastAPI, UploadFile, File, HTTPException
import pandas as pd
from app.utils import process_student_data

app = FastAPI(
    title="Student Result Analyzer",
    description="API for analyzing student performance",
    version="1.0.0"
)

REQUIRED_COLUMNS = ["math", "english", "physics"]

@app.get("/")
def home():
    return {
        "message": "Student Result Analyzer API running successfully"
    }

@app.post("/analyze")
async def analyze_results(file: UploadFile = File(...)):
    try:
        df = pd.read_csv(file.file)

        missing_columns = [
            col for col in REQUIRED_COLUMNS
            if col not in df.columns
        ]

        if missing_columns:
            raise HTTPException(
                status_code=400,
                detail=f"Missing required columns: {missing_columns}"
            )

        processed_df = process_student_data(df)

        results = processed_df.to_dict(orient="records")

        return {
            "status": "success",
            "total_students": len(results),
            "results": results
        }

    except HTTPException as http_error:
        raise http_error

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
