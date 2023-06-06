#!/usr/bin/python3

def uppercase(str):
    for char in str:
        ascii_value = ord(char)
        if 97 <= ascii_value <= 122:  # Check if lowercase character
            uppercase_char = chr(ascii_value - 32)  # Convert to uppercase
        else:
            uppercase_char = char
        print(uppercase_char, end='')
    print()
