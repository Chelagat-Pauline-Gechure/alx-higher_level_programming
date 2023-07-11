#!/usr/bin/python3
"""
Module:101-stats
Reads stdin line by line and computes metrics
"""


def print_stats(file_size, status_code_counts):
    """
    Print accumulated metrics.
    Args:
        filey_size (int): Accumulated read file size.
        status_code_counts (dict): Accumulated count of status codes.
    """
    print("File size: {}".format(file_size))
    for key in sorted(status_code_counts):
        print("{}: {}".format(key, status_code_counts[key]))


if __name__ == "__main__":
    import sys

    file_size = 0
    status_code_counts = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if current_count == 10:
                print_stats(file_size, status_code_counts)
                current_count = 1
            else:
                current_count += 1

            line = line.split()

            try:
                file_size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if status_code_counts.get(line[-2], -1) == -1:
                        status_code_counts[line[-2]] = 1
                    else:
                        status_code_counts[line[-2]] += 1
            except IndexError:
                pass

        print_stats(file_size, status_code_counts)

    except KeyboardInterrupt:
        print_stats(file_size, status_code_counts)
        raise
