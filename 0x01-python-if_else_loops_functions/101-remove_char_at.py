#!/usr/bin/python3
def remove_char_at(string, n):
    if n < 0 or n >= len(string):
        return string  # Return the original string if the index is out of bounds

    return string[:n] + string[n+1:]
