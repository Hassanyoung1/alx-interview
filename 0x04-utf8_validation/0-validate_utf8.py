#!/usr/bin/python3

"""
A method that determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Check if data is valid UTF-8 encoding.

    Parameters:
        data (list): A list of integers representing a data set.

    Returns:
        bool: True if the data represents a valid UTF-8 encoding,
        False otherwise.
    """
    num_bytes = 0

    for num in data:
        binary_representation = format(num, '#010b')[-8:]

        if num_bytes == 0:
            for bit in binary_representation:
                if bit == '0':
                    break
                num_bytes += 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (binary_representation[0] == '1' and
                    binary_representation[1] == '0'):
                return False

        num_bytes -= 1

    return num_bytes == 0
