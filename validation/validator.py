from logging_config.logger import get_logger

logger = get_logger("validation.validator")


def validate_record(record):
    """
    Validates a single record.
    Returns:
        (True, None) if valid
        (False, reason) if invalid
    """

    required_fields = ["id", "name", "age"]

    for field in required_fields:
        if field not in record:
            return False, f"Missing required field: {field}"

    if not isinstance(record["name"], str) or not record["name"].strip():
        return False, "Invalid name value"

    try:
        age = int(record["age"])
        if age <= 0:
            return False, "Age must be positive"
    except (ValueError, TypeError):
        return False, "Age must be an integer"

    return True, None
