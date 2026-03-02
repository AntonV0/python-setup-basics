"""Assignment: Log File Processor"""
from pathlib import Path
import json


def process_log_file(server_log_path, errors_log_path, summary_json_path):
    """
    Process the server log file to extract error messages, write them to 
    a new file, and create a summary JSON file with error counts.
    Args:
        server_log_path (Path): Path to the input server log file.
        errors_log_path (Path): Path to the output file for error messages.
        summary_json_path (Path): Path to the output JSON file for error summary.
    Returns:
          dict: A dictionary with error messages as keys and their counts as values.
    """
    error_counts = {}  # Dictionary to hold error message as key and count as value

    try:
        # Open the server log file for reading and the errors log file for writing
        with open(server_log_path, "r", encoding="utf-8") as src, \
                open(errors_log_path, "w", encoding="utf-8") as err_out:

            # Read the server log file line by line
            for line in src:
                # Strip whitespace and skip empty lines
                line = line.strip()
                if not line:
                    continue

                # Format: DATE TIME LEVEL MESSAGE
                # Split into 4 parts: date, time, level, and message
                parts = line.split(" ", 3)
                if len(parts) < 4:  # If the line doesn't have enough parts, skip it
                    continue

                # Unpack the parts into variables
                level = parts[2]
                message = parts[3]

                if level == "ERROR":
                    # Write full error line
                    err_out.write(line + "\n")

                    # Count the message only
                    error_counts[message] = error_counts.get(message, 0) + 1

        # Write summary JSON
        with open(summary_json_path, "w", encoding="utf-8") as f:
            # Convert dictionary to JSON string and save
            json.dump(error_counts, f, indent=4)

        return error_counts

    except IOError as e:
        print(f"IOError: {e}")
        return None


def main():
    """Main function to execute the log processing."""
    base_dir = Path(__file__).parent

    # Define paths for I/O files in the same directory as the script
    server_log = base_dir / "server.log"
    errors_log = base_dir / "errors.log"
    summary_json = base_dir / "error_summary.json"

    # Process the log file and get the error counts
    result = process_log_file(server_log, errors_log, summary_json)

    # If processing was successful, print the results
    if result is not None:
        print("Done.")
        print(f"Errors written to: {errors_log.name}")
        print(f"Summary written to: {summary_json.name}")
        print("\nError counts:")

        # Print each error message and its count in a readable format
        for msg, count in result.items():
            print(f"- {msg}: {count}")


if __name__ == "__main__":
    main()


# ? Logs in server.log:
# 2026-03-02 10:15:32 INFO Server started successfully
# 2026-03-02 10:16:01 INFO User login successful: user_id=1
# 2026-03-02 10:17:45 ERROR Database connection failed
# 2026-03-02 10:18:12 WARNING High memory usage detected
# 2026-03-02 10:19:03 ERROR Database connection failed
# 2026-03-02 10:20:55 INFO File uploaded successfully
# 2026-03-02 10:22:10 ERROR Invalid API key provided
# 2026-03-02 10:23:01 ERROR Database connection failed

# ? Output in errors.log:
# 2026-03-02 10:17:45 ERROR Database connection failed
# 2026-03-02 10:19:03 ERROR Database connection failed
# 2026-03-02 10:22:10 ERROR Invalid API key provided
# 2026-03-02 10:23:01 ERROR Database connection failed

# ? Output in error_summary.json:
# {
#     "Database connection failed": 3,
#     "Invalid API key provided": 1
# }
