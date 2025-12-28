from logging_config.logger import get_logger
from validation.validator import validate_record
from ingestion.reader import read_csv_file, read_json_file

# Initialize logger for this module
logger = get_logger("main")

def main():
    logger.info("Application started")

    # -------------------
    # CSV ingestion test
    # -------------------
    logger.info("Starting CSV ingestion...")

    csv_valid_count = 0

    for row in read_csv_file("data/raw/sample.csv"):
     for valid_row in validate_record(row):
        logger.info(f"Valid CSV record: {valid_row}")
        csv_valid_count += 1

    logger.info(f"Total valid CSV records: {csv_valid_count}")


    # -------------------
    # JSON ingestion test
    # -------------------
logger.info("Starting JSON ingestion...")

json_valid_count = 0

for record in read_json_file("data/raw/sample.json"):
    for valid_record in validate_record(record):
        logger.info(f"Valid JSON record: {valid_record}")
        json_valid_count += 1

logger.info(f"Total valid JSON records: {json_valid_count}")


if __name__ == "__main__":
    main()
