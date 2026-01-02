import os
# Used to read environment variables

# -----------------------
# Environment
# -----------------------

ENV = os.getenv("PYDATAFLOW_ENV", "DEV")
# If PYDATAFLOW_ENV is not set, default to DEV

# -----------------------
# Retry configuration
# -----------------------

MAX_RETRIES = 3 if ENV == "DEV" else 5
# Fewer retries in DEV (faster feedback)
# More retries in PROD (more stability)

RETRY_BACKOFF_BASE = 2
# Base for exponential backoff (2^n)

# -----------------------
# Paths
# -----------------------

RAW_DATA_PATH = "data/raw"
# Central raw data location

REJECTED_DATA_PATH = "data/rejected/rejected_records.jsonl"
# Rejected records storage path

# -----------------------
# Logging
# -----------------------

LOG_LEVEL = "DEBUG" if ENV == "DEV" else "INFO"
# Verbose logs in DEV
# Cleaner logs in PROD
