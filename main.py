from logging_config.logger import get_logger
from ingestion.reader import read_csv_file, read_json_file

# Initialize logger for this module
logger = get_logger("main")

def main():
    logger.info("Application started")

    # -------------------
    # CSV ingestion test
    # -------------------
    logger.info("Starting CSV ingestion...")
    try:
        for row in read_csv_file("data/raw/sample.csv"):
            logger.info(f"CSV row: {row}")
    except FileNotFoundError as e:
        logger.error(f"CSV ingestion failed: {e}")

    # -------------------
    # JSON ingestion test
    # -------------------
    logger.info("Starting JSON ingestion...")
    try:
        for record in read_json_file("data/raw/sample.json"):
            logger.info(f"JSON record: {record}")
    except (FileNotFoundError, ValueError) as e:
        logger.error(f"JSON ingestion failed: {e}")

    logger.info("Application finished successfully")

if __name__ == "__main__":
    main()
