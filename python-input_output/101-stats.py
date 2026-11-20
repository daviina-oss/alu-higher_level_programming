#!/usr/bin/python3
"""Module 101-stats: reads log lines from stdin and computes metrics.

Input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

Every 10 lines, and after a keyboard interruption (CTRL + C), the statistics
since the beginning are printed.
"""
import sys


def print_stats(total_size, status_counts):
    """Print the total file size and the number of lines per status code."""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts):
        print("{}: {}".format(code, status_counts[code]))


if __name__ == "__main__":
    valid_codes = ("200", "301", "400", "401", "403", "404", "405", "500")
    total_size = 0
    status_counts = {}
    count = 0
    try:
        for line in sys.stdin:
            count += 1
            parts = line.split()
            try:
                size = int(parts[-1])
                code = parts[-2]
            except (IndexError, ValueError):
                size = None
            if size is not None:
                total_size += size
                if code in valid_codes:
                    status_counts[code] = status_counts.get(code, 0) + 1
            if count % 10 == 0:
                print_stats(total_size, status_counts)
        if count == 0 or count % 10 != 0:
            print_stats(total_size, status_counts)
    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise
