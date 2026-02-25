"""Exercise 1: Simple Text File Logger"""

from pathlib import Path  # To create log file in the same directory as this script
from datetime import datetime  # To add timestamps to log entries

# User input for the log message
log_text = input("Please write a single line of text to log: ")

try:
    # Get the folder where this script lives
    base_dir = Path(__file__).parent
    # Define the path to the log file in the same directory as the script
    log_file_path = base_dir / "log.txt"

    # Open the log file in append mode and write the log message with a timestamp
    with open(log_file_path, "a", encoding="utf-8") as log_file:
        # Format the current date and time as a string
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Write the log message to the file in the format: [timestamp] log_text
        log_file.write(f"[{timestamp}] {log_text}\n")

    print("Your text has been logged successfully.")

except IOError as e:
    print(f"An error occurred while writing to the log file: {e}")

# ? Output in terminal:
# Please write a single line of text to log: This is the first sentence
# Your text has been logged successfully.

# Please write a single line of text to log: This is another sentence
# Your text has been logged successfully.

# Please write a single line of text to log: This is the third sentence
# Your text has been logged successfully.

# ? Output in log.txt:
# [2026-02-25 16:14:24] This is the first sentence
# [2026-02-25 16:14:39] This is another sentence
# [2026-02-25 16:14:48] This is the third sentence
