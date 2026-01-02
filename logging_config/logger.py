import logging
# Python built-in logging module

from config.settings import LOG_LEVEL
# Import log level from config (DEV / PROD aware)

def get_logger(name: str):
    """
    Returns a configured logger instance.
    """

    logger = logging.getLogger(name)
    # Get (or create) a logger with the given name

    if logger.handlers:
        return logger
        # Prevent duplicate handlers if logger already exists

    level = getattr(logging, LOG_LEVEL)
    # Convert "DEBUG"/"INFO" string into logging.DEBUG / logging.INFO

    logger.setLevel(level)
    # Set logger level based on environment

    handler = logging.StreamHandler()
    # Log output to console (stdout)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    # Define log format

    handler.setFormatter(formatter)
    # Attach format to handler

    logger.addHandler(handler)
    # Attach handler to logger

    return logger
