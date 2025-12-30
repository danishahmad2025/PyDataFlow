from logging_config.logger import get_logger
from ingestion.reader import read_csv_file, read_json_file
from validation.validator import validate_record
from storage.rejected_writer import write_rejected_record

logger = get_logger("main")

def main():
    logger.info("Application started")

    # -----------------------
    # Global counters
    # -----------------------
    total_records = 0
    valid_records = 0
    rejected_records = 0

    csv_records = 0
    json_records = 0

    # -----------------------
    # CSV ingestion
    # -----------------------
    logger.info("Starting CSV ingestion")
    source = "csv"

    for record in read_csv_file("data/raw/sample.csv"):
        total_records += 1
        csv_records += 1

        is_valid, error = validate_record(record)

        if is_valid:
            valid_records += 1
            logger.info(f"Valid CSV record: {record}")
        else:
            rejected_records += 1
            write_rejected_record(record, error, source)

    # -----------------------
    # JSON ingestion
    # -----------------------
    logger.info("Starting JSON ingestion")
    source = "json"
    for record in read_json_file("data/raw/sample.json"):
        total_records += 1
        json_records += 1

        is_valid, error = validate_record(record)

        if is_valid:
            valid_records += 1
            logger.info(f"Valid JSON record: {record}")
        else:
            rejected_records += 1
            write_rejected_record(record, error, source)

    # -----------------------
    # Final summary
    # -----------------------
    logger.info("Pipeline execution summary")
    logger.info(f"Total records processed: {total_records}")
    logger.info(f"Valid records: {valid_records}")
    logger.info(f"Rejected records: {rejected_records}")
    logger.info(f"CSV records: {csv_records}")
    logger.info(f"JSON records: {json_records}")

    logger.info("Application finished successfully")

if __name__ == "__main__":
    main()
