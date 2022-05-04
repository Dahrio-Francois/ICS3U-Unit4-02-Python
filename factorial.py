#!/usr/bin/env python3

# Created by: Dahrio Francois
# Created on: April 2022
# This program calculates the factorials of numbers
#   inputted by the user

import math


def main():
    # this creates the factorial program

    # input
    integer = int(input("Enter in an integer to be multiplied by factorials: "))

    factorial = 1

    # process
    if integer < 0:
        print("\nFactorial does not exist for negative numbers.")
    elif integer == 0:
        print("\nThe factorial of 0 is 1.")
    else:
        for i in range(1, integer + 1):
            factorial = factorial * i
        print("\nThe factorial of", integer, "is", factorial)


if __name__ == "__main__":
    main()
