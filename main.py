# Import logger factory
from logging_config.logger import get_logger

# Import ingestion functions
from ingestion.reader import read_csv_file, read_json_file

# Import validation function
from validation.validator import validate_record

# Import rejected record writer
from storage.rejected_writer import write_rejected_record

# Import metrics class
from metrics.metrics import PipelineMetrics

from reprocessing.reprocess_rejected import reprocess_rejected

reprocess_rejected()



# Create logger for main module
logger = get_logger("main")


def main():
    """
    Main entry point of the PyDataFlow pipeline.
    This function orchestrates the entire flow.
    """

    # Log application start
    logger.info("Application started")

    # -----------------------
    # Initialize metrics
    # -----------------------

    # Create metrics object to track pipeline behavior
    metrics = PipelineMetrics()

    # -----------------------
    # CSV ingestion
    # -----------------------

    logger.info("Starting CSV ingestion")

    # Read CSV file record by record (generator)
    for record in read_csv_file("data/raw/sample.csv"):

        # Every record counts as total
        metrics.increment_total()

        # Record source is CSV
        metrics.increment_csv()

        # Validate the record
        is_valid, error = validate_record(record)

        if is_valid:
            # Record passed validation
            metrics.increment_valid()

            # Log valid record
            logger.info(f"Valid CSV record: {record}")

        else:
            # Record failed validation
            metrics.increment_rejected()

            # Store rejected record with reason and source
            write_rejected_record(
                record=record,
                reason=error,
                source="csv"
            )

    # -----------------------
    # JSON ingestion
    # -----------------------

    logger.info("Starting JSON ingestion")

    # Read JSON file record by record (generator)
    for record in read_json_file("data/raw/sample.json"):

        # Increment total records
        metrics.increment_total()

        # Record source is JSON
        metrics.increment_json()

        # Validate the record
        is_valid, error = validate_record(record)

        if is_valid:
            # Record passed validation
            metrics.increment_valid()

            # Log valid record
            logger.info(f"Valid JSON record: {record}")

        else:
            # Record failed validation
            metrics.increment_rejected()

            # Store rejected record with reason and source
            write_rejected_record(
                record=record,
                reason=error,
                source="json"
            )

    # -----------------------
    # Final metrics summary
    # -----------------------

    logger.info("Pipeline execution summary")

    # Iterate over metrics summary and log each value
    for key, value in metrics.summary().items():
        logger.info(f"{key}: {value}")

    # Log successful completion
    logger.info("Application finished successfully")


# Standard Python entry-point check
if __name__ == "__main__":
    main()
