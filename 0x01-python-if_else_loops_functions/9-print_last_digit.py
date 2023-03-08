#!/usr/bin/python3
def print_last_digit(n):
    last_digit = (n % 10) if n >= 0 else ((n * -1) % 10)
    print(last_digit, end='')
    return (last_digit)
