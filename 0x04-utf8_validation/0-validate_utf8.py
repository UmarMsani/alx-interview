#!/usr/bin/python3
"""
UTF-8 validation module.
"""


def validUTF8(data):
    """
    Determine if a given dataset represents a valid UTF-8 encoding.

    :param data: List of integers representing bytes of data
    :return: True if data is a valid UTF-8 encoding, else False
    """

    # Iterate through the data bytes
    byte_count = 0

    for j in data:
        if byte_count == 0:
            if j >> 5 == 0b110 or j >> 5 == 0b1110:
                byte_count = 1
            elif j >> 4 == 0b1110:
                byte_count = 2
            elif j >> 3 == 0b11110:
                byte_count = 3
            elif j >> 7 == 0b1:
                return False
        else:
            if j >> 6 != 0b10:
                return False
            byte_count -= 1
    return byte_count == 0
