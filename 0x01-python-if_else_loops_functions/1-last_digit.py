#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# find the last digit of number

if number > 0:
    last_digit = abs(number) % 10
else:
    last_digit = -1 * (abs(number) % 10)

print(f"Last digit of {number} is {last_digit} and is", end=" ")
# if the last digit is greater than 5 print it
if last_digit > 5:
    print("greater than 5")

# if the last digit is zero print it
elif last_digit == 0:
    print("0")

# if the last digit is less than 6 and not 0
elif last_digit < 6 and last_digit != 0:
    print("less than 6 and not 0")
