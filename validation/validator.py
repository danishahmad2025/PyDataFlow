from logging_config.logger import get_logger
logger = get_logger("validation.validator")
def validate_record(record):
    """
    Validates a single record.
    Yields the record only if it is valid.
    """
    required_fields = ["id", "name", "age"]

    for field in required_fields:
        if field not in record:
            logger.warning(f"Missing required field '{field}' in record: {record}")
            return

    if not isinstance(record["name"],str) or not record["name"].strip():
        logger.warning(f"Invalid name value:{record}")
        return
    

    try:
        age = int(record["age"])
        if age <= 0:
            raise ValueError
    except (ValueError, TypeError):
        logger.warning(f"Invalid age value: {record}")
        return
    
    yield record