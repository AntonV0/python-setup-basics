"""Log writer module for reusable logging configuration."""


def log_writer(logger, message, level):
    """Writes a log message using the provided logger to a file"""
    # Level is the severity of the log message, which determines how it will be recorded
    # and displayed.
    if level == "debug":
        logger.debug(message)
    elif level == "info":
        logger.info(message)
    elif level == "warning":
        logger.warning(message)
    elif level == "error":
        logger.error(message)
    elif level == "critical":
        logger.critical(message)
    else:
        raise ValueError("Invalid log level specified.")
