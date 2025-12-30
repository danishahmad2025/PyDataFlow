from logging_config.logger import get_logger
from ingestion.reader import read_csv_file, read_json_file
from validation.validator import validate_record
from storage.rejected_writer import write_rejected_record

logger = get_logger("main")


def main():
    logger.info("Application started")

    logger.info("Starting CSV ingestion")
    for record in read_csv_file("data/raw/sample.csv"):
        is_valid, error = validate_record(record)

        if is_valid:
            logger.info(f"Valid CSV record: {record}")
        else:
            write_rejected_record(record, error, "csv")

    logger.info("Starting JSON ingestion")
    for record in read_json_file("data/raw/sample.json"):
        is_valid, error = validate_record(record)

        if is_valid:
            logger.info(f"Valid JSON record: {record}")
        else:
            write_rejected_record(record, error, "json")

    logger.info("Application finished successfully")


if __name__ == "__main__":
    main()
