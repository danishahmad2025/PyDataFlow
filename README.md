PyDataFlow 🚀

A beginner-friendly, production-style Python data ingestion pipeline.

📌 Project Overview

PyDataFlow is a mini data engineering project that demonstrates how real-world data pipelines are built using pure Python.

The project focuses on:

Streaming data ingestion

Data validation

Safe handling of bad data

Logging and metrics

Clean, modular project structure

This repository is designed for learning, revision, and contribution.

🎯 What This Project Does

Reads data from CSV and JSON files

Processes records one by one using generators (memory-efficient)

Validates each record without breaking the pipeline

Separates valid and rejected records

Stores rejected records with detailed reasons

Tracks metrics like total, valid, and rejected records

Logs everything for easy debugging and observability

🧠 Why This Project Matters

In real data systems:

Data is often messy

Pipelines must not crash due to bad records

Logging and metrics are critical

Code must be modular and scalable

PyDataFlow simulates these real-world challenges in a simple and understandable way.

🏗️ Project Structure
PyDataFlow/
│
├── ingestion/           # Reading data sources (CSV, JSON)
││   ├── __init__.py
││   └── reader.py
│
├── validation/          # Data validation logic
││   ├── __init__.py
││   └── validator.py
│
├── storage/             # Storing rejected records
││   ├── __init__.py
││   └── rejected_writer.py
│
├── logging_config/      # Centralized logging setup
││   ├── __init__.py
││   └── logger.py
│
├── data/
││   ├── raw/            # Input data files
││   └── rejected/       # Rejected records (not committed)
│
├── utils/               # Utilities (retry, metrics, helpers)
│
├── main.py              # Pipeline entry point
├── requirements.txt
└── README.md

🔧 Technologies Used

Python

Python Logging module

Generators & Iterators

File-based data processing (CSV, JSON, JSONL)

Modular pipeline architecture

Git & GitHub

⚠️ Note: This project intentionally avoids Pandas to demonstrate streaming data processing.

▶️ How to Run the Project

Clone the repository

git clone https://github.com/<your-username>/PyDataFlow.git
cd PyDataFlow


(Optional but recommended) Create a virtual environment

python -m venv venv
source venv/bin/activate


Install dependencies

pip install -r requirements.txt


Run the pipeline

python main.py

📊 Output You Will See

Logs printed in terminal and stored in log files

Valid records processed successfully

Invalid records written to:

data/rejected/rejected_records.jsonl


Final summary with processing metrics

🧪 Example Rejected Record (JSONL)
{
  "timestamp": "2025-12-30T19:18:49",
  "source": "csv",
  "reason": "Invalid age value",
  "record": {"id": "5", "name": "David", "age": "-5"}
}

🌱 Future Improvements

Add database storage (SQLite / PostgreSQL)

Add Pandas-based transformations

Add unit tests

Add orchestration (Airflow / Prefect)

Add API ingestion

🤝 Contributions

This project is open-source and contribution-friendly.

Feel free to:

Fork the repo

Open issues

Submit pull requests

Suggest improvements

📌 Author

Danish Ekbal Ahmad
Learning Data Engineering by building real projects.
