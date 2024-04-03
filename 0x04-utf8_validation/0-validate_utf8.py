#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Determine if a given dataset represents a valid UTF-8 encoding.

    :param data: List of integers representing bytes of data
    :return: True if data is a valid UTF-8 encoding, else False
    """

    def is_start_of_char(byte):
        """
        Check if the given byte is the start of a UTF-8 character.
        :param byte: Integer representing a byte
        :return: True if byte is the start of a UTF-8 character, else False
        """
        return (byte >> 7 == 0) or \
               (byte >> 5 == 6 and byte & 0b11111 <= 0b11111) or \
               (byte >> 4 == 14 and byte & 0b1111 <= 0b111) or \
               (byte >> 3 == 30 and byte & 0b111 <= 0b11)

    # Iterate through the data bytes
    i = 0
    while i < len(data):
        # Check if the byte is the start of a character
        if not is_start_of_char(data[i]):
            return False

        # Determine the number of bytes in the character
        if data[i] >> 7 == 0:
            char_length = 1
        elif data[i] >> 5 == 6:
            char_length = 2
        elif data[i] >> 4 == 14:
            char_length = 3
        elif data[i] >> 3 == 30:
            char_length = 4
        else:
            return False

        # Check if the subsequent bytes are continuation bytes
        for j in range(1, char_length):
            if i + j >= len(data) or not (data[i + j] >> 6 == 2):
                return False
        i += char_length

    return True
