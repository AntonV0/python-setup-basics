"""Log setup module for reusable logging configuration."""

import logging  # Built-in module for logging in Python
from pathlib import Path  # Built-in module for handling file paths


def configure_logger(logger_name, log_file="app.log", level="DEBUG"):
    """Configures a logger with the specified name, log file, and logging level."""
    logger = logging.getLogger(logger_name)

    # Convert the string log level to a numeric value recognised by the logging module
    numeric_level = getattr(logging, level.upper(), logging.INFO)
    logger.setLevel(numeric_level)

    # Avoid adding handlers twice
    if logger.handlers:
        return logger

    # Define a log message format that includes the timestamp, logger name, log level, and message
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Put log file inside this package folder
    package_dir = Path(__file__).resolve().parent
    log_path = package_dir / log_file

    # Create a file handler that writes log messages to the specified log file with UTF-8 encoding
    fh = logging.FileHandler(log_path, encoding="utf-8")
    fh.setLevel(numeric_level)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger  # Return the configured logger instance for use in other modules
