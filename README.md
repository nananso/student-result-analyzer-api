# Student Result Analyzer API

A professional FastAPI-based backend application for analyzing student academic performance from uploaded CSV files.

## Features

* Upload CSV files through API
* Calculate student averages
* Assign grades automatically
* Validate uploaded datasets
* Handle missing columns professionally
* Swagger API documentation
* JSON-based API responses

---

## Tech Stack

* Python
* FastAPI
* Pandas
* Uvicorn
* Git & GitHub

---

## Project Structure

```bash
week1-student-result-analyzer/
│
├── app/
│   ├── main.py
│   ├── utils.py
│   └── __init__.py
│
├── data/
│   ├── students.csv
│   └── bad_students.csv
│
├── tests/
├── requirements.txt
├── Dockerfile
├── README.md
└── .gitignore
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/nananso/student-result-analyzer-api.git
```

### Navigate into the Project

```bash
cd student-result-analyzer-api
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the API

```bash
uvicorn app.main:app --reload
```

---

## API Documentation

After starting the server, open:

```bash
http://127.0.0.1:8000/docs
```

---

## Sample CSV Format

```csv
name,math,english,physics
John,80,75,90
Mary,65,70,60
David,90,88,95
Grace,50,45,55
```

---

## Example API Response

```json
{
  "status": "success",
  "total_students": 4,
  "results": [
    {
      "name": "John",
      "math": 80,
      "english": 75,
      "physics": 90,
      "average": 81.67,
      "grade": "A"
    }
  ]
}
```

---

## Future Improvements

* Pytest automated testing
* Docker containerization
* CI/CD pipelines
* Cloud deployment
* Machine learning integration
* Monitoring and logging

---

## Author

Uchenna Nsoha
Aspiring MLOps Engineer & Backend Developer
