from logging_config.logger import get_logger

logger = get_logger("main")

def main():
    logger.info("Application started")
    logger.debug("This is a debug message")
    logger.warning("This is a warning")
    logger.error("This is an error message")

if __name__ == "__main__":
    main()
