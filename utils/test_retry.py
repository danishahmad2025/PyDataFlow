from retry.retry_handler import retry_operation
from logging_config.logger import get_logger

logger = get_logger("test.retry")

# A counter to simulate failure then success
attempt_counter = {"count": 0}

def flaky_function():
    """
    This function fails twice and succeeds on the 3rd attempt.
    """
    attempt_counter["count"] += 1

    if attempt_counter["count"] < 3:
        raise RuntimeError("Temporary failure")

    return "SUCCESS"


if __name__ == "__main__":
    result = retry_operation(flaky_function, max_retries=3)
    logger.info(f"Final result: {result}")
