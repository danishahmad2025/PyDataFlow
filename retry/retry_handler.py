import time
from logging_config.logger import get_logger

logger = get_logger("retry.retry_handler")


def retry_operation(operation, max_retries=3, retry_exceptions=(Exception,)):
    """
    Retries a given operation with exponential backoff.

    Parameters:
    - operation: function to retry
    - max_retries: number of attempts
    - retry_exceptions: exceptions that trigger retry

    Returns:
    - result of operation if successful

    Raises:
    - last exception if all retries fail
    """

    attempt = 0

    while attempt < max_retries:
        try:
            logger.info(f"Attempt {attempt + 1} of {max_retries}")
            return operation()

        except retry_exceptions as e:
            attempt += 1

            if attempt == max_retries:
                logger.error("Max retries reached. Giving up.")
                raise

            backoff_time = 2 ** attempt
            logger.warning(
                f"Operation failed: {e}. Retrying in {backoff_time} seconds..."
            )

            time.sleep(backoff_time)

