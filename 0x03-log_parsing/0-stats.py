#!/usr/bin/python3
"""
module: 0-stats
"""
import sys
import re
import signal


status_code_counts = {
    200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
}

total_file_size = 0

line_count = 0


def signal_handler(sig, frame):
    """Signal handler to handle keyboard interruption."""
    print_stats()
    sys.exit(0)


def parse_log_line(line):
    """
    Parse a log line and update metrics.

    Parameters:
        line (str): The log line to parse.

    Returns:
        None
    """
    global total_file_size, line_count
    pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' \
              r' - \[.*\]' \
              r' "GET \/projects\/260 HTTP\/1\.1"' \
              r' (\d{3}) (\d+)$'

    match = re.match(pattern, line)
    if match:
        status_code = int(match.group(2))
        file_size = int(match.group(3))
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1
        total_file_size += file_size
        line_count += 1
    else:
        # Print an error message to stderr indicating the skipped line
        sys.stderr.write(f"Skipped line: {line}\n")


def print_stats():
    """Print statistics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")


signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    parse_log_line(line.strip())
    if line_count % 10 == 0 and line_count != 0:
        print_stats()

# Print statistics for remaining lines if less than 10 lines are processed
if line_count > 0:
    print_stats()

# Print statistics even if there is no input
if line_count == 0:
    print_stats()
