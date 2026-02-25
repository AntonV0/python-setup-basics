"""Assignment: Reusable Logging Package."""

from reusable_logging_package.log_setup import configure_logger
from reusable_logging_package.log_writer import log_writer


def main():
    """Main function to demonstrate reusable logging."""
    # Configure the logger using the log_setup module and create a logger instance
    logger = configure_logger("my_logger", "app.log", "DEBUG")

    # Use the log_writer function to write log messages of various levels to the log file
    log_writer(logger, "This is a debug message.", "debug")
    log_writer(logger, "This is an info message.", "info")
    log_writer(logger, "This is a warning message.", "warning")
    log_writer(logger, "This is an error message.", "error")
    log_writer(logger, "This is a critical message.", "critical")


if __name__ == "__main__":
    main()

# ? Output in app.log:
# 2026-02-25 11:08:37,330 - my_logger - DEBUG - This is a debug message.
# 2026-02-25 11:08:37,330 - my_logger - INFO - This is an info message.
# 2026-02-25 11:08:37,330 - my_logger - WARNING - This is a warning message.
# 2026-02-25 11:08:37,330 - my_logger - ERROR - This is an error message.
# 2026-02-25 11:08:37,330 - my_logger - CRITICAL - This is a critical message.
