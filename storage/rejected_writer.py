import json
import os
from datetime import datetime
from logging_config.logger import get_logger

# Create logger for rejected writer
logger = get_logger("storage.rejected_writer")


def write_rejected_record(record, reason, source):
    """
    Writes rejected records to a JSON Lines file (JSONL).

    This function is:
    - append-only
    - safe for reprocessing
    - retry-friendly
    """

    # Ensure rejected directory exists (idempotent operation)
    os.makedirs("data/rejected", exist_ok=True)

    # Build rejected entry structure
    rejected_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "source": source,
        "reason": reason,
        "record": record
    }

    try:
        # Open file in append mode
        with open("data/rejected/rejected_records.jsonl", "a") as f:
            # Write one JSON object per line
            f.write(json.dumps(rejected_entry) + "\n")

        # Warning level because this is abnormal but expected behavior
        logger.warning(f"Rejected record stored: {rejected_entry}")

    except Exception as e:
        # Log error but DO NOT crash pipeline
        logger.error(f"Failed to write rejected record: {e}")
