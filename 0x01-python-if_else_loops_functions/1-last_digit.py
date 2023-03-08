#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_to_string = repr(number)
last_digit_string = number_to_string[-1]
if int(last_digit_string) > 5:
    print(f"Last digit of {number} is {last_digit_string} and is greater than 5")
elif int(last_digit_string) <6 and int(last_digit_string) != 0:
    print(f"Last digit of {number} is {last_digit_string} and is less than 6 and not 0")
elif int(last_digit_string) == 0:
    print(f"Last digit of {number} is {last_digit_string} and is 0")
elif int(last_digit_string) < 0 and int(last_digit_string) <6 and int(last_digit_string) != 0:
    print(f"Last digit of {number} is -{last_digit_string} and is less than 6 and not 0")