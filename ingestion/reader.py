from pathlib import Path
import csv
import json
from typing import Generator, Dict, Any

from logging_config.logger import get_logger

logger = get_logger("ingestion.reader")


def read_csv_file(file_path: str) -> Generator[Dict[str, Any], None, None]:
    """
    Reads a CSV file row by row using a generator.
    """
    path = Path(file_path)

    if not path.exists():
        logger.error(f"CSV file not found: {file_path}")
        raise FileNotFoundError(file_path)

    logger.info(f"Reading CSV file: {file_path}")

    with path.open(mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        empty = True

        for row in reader:
            empty = False
            logger.debug(f"Read CSV row: {row}")
            yield row
        if empty:
         logger.warning(f"CSV file is empty: {file_path}")


def read_json_file(file_path: str) -> Generator[Dict[str, Any], None, None]:
    """
    Reads a JSON file containing a list of records.
    """
    path = Path(file_path)

    if not path.exists():
        logger.error(f"JSON file not found: {file_path}")
        raise FileNotFoundError(file_path)

    logger.info(f"Reading JSON file: {file_path}")

    with path.open(mode="r", encoding="utf-8") as file:
        data = json.load(file)
    if not data:
        logger.warning(f"JSON file is empty: {file_path}")
    for record in data:
        yield record

        if not isinstance(data, list):
            logger.error("JSON file must contain a list of objects")
            raise ValueError("Invalid JSON structure")

        for record in data:
            logger.debug(f"Read JSON record: {record}")
            yield record
