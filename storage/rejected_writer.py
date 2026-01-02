import json
# Used to serialize Python dicts into JSON

import os
# Used for directory creation

from datetime import datetime
# Used for timestamping rejected records

from logging_config.logger import get_logger
# Project logger

from config.settings import REJECTED_DATA_PATH
# Central rejected path from config

logger = get_logger("storage.rejected_writer")


def write_rejected_record(record, reason, source):
    """
    Writes rejected records as JSON Lines (JSONL).
    """

    # Ensure directory exists (important for first run)
    os.makedirs(os.path.dirname(REJECTED_DATA_PATH), exist_ok=True)

    rejected_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        # When the rejection happened (UTC)

        "source": source,
        # Where the record came from (csv/json/api)

        "reason": reason,
        # Why it was rejected

        "record": record
        # Actual rejected data
    }

    try:
        with open(REJECTED_DATA_PATH, "a") as file:
            file.write(json.dumps(rejected_entry) + "\n")
            # Append one JSON object per line

        logger.warning(f"Rejected record stored: {rejected_entry}")

    except Exception as exc:
        logger.error(f"Failed to write rejected record: {exc}")
