# PyDataFlow 🚀

A beginner-friendly, production-style **Python data ingestion pipeline**.

---

## 📌 Project Overview

**PyDataFlow** is a mini data engineering project that demonstrates how
real-world data pipelines are built using **pure Python**.

This project is designed for:
- Learning core data engineering concepts
- Practicing clean project structure
- Understanding streaming-style pipelines
- Revision and open-source contribution

---

## 🎯 What This Project Does

- Reads data from **CSV** and **JSON** files
- Processes records **one at a time** using generators (memory efficient)
- Validates each record safely without stopping the pipeline
- Separates **valid** and **rejected** records
- Stores rejected records with detailed rejection reasons
- Tracks basic processing metrics
- Logs every important step for debugging and observability

---

## 🧠 Why This Project Matters

In real-world data systems:

- Data is often **messy or incomplete**
- Pipelines **must not crash** because of bad records
- Logging and metrics are essential for debugging
- Code must be **modular, readable, and scalable**

**PyDataFlow simulates these real-world challenges** in a simple and easy-to-understand way.

---

## 🏗️ Project Structure

PyDataFlow/
│
├── ingestion/ # Reading data sources
│ ├── init.py
│ └── reader.py # CSV & JSON readers (generators)
│
├── validation/ # Data validation logic
│ ├── init.py
│ └── validator.py
│
├── storage/ # Handling rejected records
│ ├── init.py
│ └── rejected_writer.py
│
├── logging_config/ # Centralized logging setup
│ ├── init.py
│ └── logger.py
│
├── data/
│ ├── raw/ # Input data files
│ └── rejected/ # Rejected records (not committed)
│
├── utils/ # Utilities (retry, metrics, helpers)
│
├── main.py # Pipeline entry point
├── requirements.txt
└── README.md

---

## 🔧 Technologies Used

- **Python**
- Python **logging** module
- Generators & iterators
- File-based processing (CSV, JSON, JSONL)
- Modular pipeline architecture
- Git & GitHub

> ⚠️ **Note:**  
> This project intentionally avoids Pandas to demonstrate
> streaming data processing and memory-efficient design.

---

## ▶️ How to Run the Project

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/PyDataFlow.git
cd PyDataFlow

---

2️⃣ (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the pipeline
python main.py

📊 Output You Will See

Logs printed in the terminal

Logs stored in log files

Valid records processed successfully

Invalid records written to:

data/rejected/rejected_records.jsonl


Final execution summary with processing metrics

🧪 Example Rejected Record (JSONL)
{
  "timestamp": "2025-12-30T19:18:49",
  "source": "csv",
  "reason": "Invalid age value",
  "record": {
    "id": "5",
    "name": "David",
    "age": "-5"
  }
}

🌱 Future Improvements

Add database storage (SQLite / PostgreSQL)

Add Pandas-based transformations

Add unit tests

Add orchestration (Airflow / Prefect)

Add API-based ingestion

🤝 Contributions

This project is open-source and contribution-friendly.

You are welcome to:

Fork the repository

Open issues

Submit pull requests

Suggest improvements

📌 Author

Danish Ekbal Ahmad
Learning Data Engineering by building real-world projects.

