import json
from logging_config.logger import get_logger
from validation.validator import validate_record

# Logger for reprocessing module
logger = get_logger("reprocessing.reprocess_rejected")


def reprocess_rejected(file_path="data/rejected/rejected_records.jsonl"):
    """
    Reads rejected records and tries to validate them again.
    """

    logger.info("Starting rejected data reprocessing")

    # Counter for tracking success
    recovered_count = 0

    try:
        # Open rejected records file
        with open(file_path, "r") as f:
            for line in f:
                # Convert JSON line back to dictionary
                rejected_entry = json.loads(line)

                # Extract original record
                record = rejected_entry["record"]

                # Validate again using latest rules
                is_valid, error = validate_record(record)

                if is_valid:
                    recovered_count += 1
                    logger.info(f"Recovered record: {record}")
                else:
                    logger.warning(
                        f"Still invalid: {record} | Reason: {error}"
                    )

    except FileNotFoundError:
        logger.warning("No rejected records file found")

    logger.info(f"Reprocessing completed. Recovered: {recovered_count}")
