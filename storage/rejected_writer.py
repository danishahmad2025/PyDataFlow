import json
from datetime import datetime
from logging_config.logger import get_logger

logger = get_logger("storage.rejected_writer")


def write_rejected_record(record, reason, source):
    """
    Writes rejected records to a JSONL (JSON Lines) file.

    Each rejected record is written as a single JSON object per line.
    """

    rejected_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "source": source,
        "reason": reason,
        "record": record
    }

    try:
        with open("data/rejected/rejected_records.jsonl", "a") as f:
            f.write(json.dumps(rejected_entry) + "\n")

        logger.warning(f"Rejected record stored: {rejected_entry}")

    except Exception as e:
        logger.error(f"Failed to write rejected record: {e}")
