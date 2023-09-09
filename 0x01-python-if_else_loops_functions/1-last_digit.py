#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number2 = abs(number)
last_digit = number2 % 10

if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and it is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and it is 0")
elif (last_digit < 6) and (last_digit != 0):
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
