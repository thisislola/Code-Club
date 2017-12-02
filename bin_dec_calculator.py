# Binary Calculator by L. Carthy

import time
import re
import sys

def intro_options():
    """ Takes the option and returns the function
    that correlates """

    option = int(input("1 for Binary to Decimal \n"
                        "2 for Decimal to Binary: "))
    if option == 1:
        binary_calc()
    elif option == 2:
        decimal_calc()
    else:
        print("That is not an option. Try again.")
        time.sleep(2)
        intro_options()

def binary_calc():
    """ Receives input in the form
    of a binary number (1's and 0's)
    and returns its decimal value."""

    decimal_value = 0    # Set to 0 to change values
    binary_input = input("Binary number: ")

    if not re.match("[0-1]", binary_input):     # It must match 0 OR 1
        print(">>> Only 1s and 0s allowed <<<")
        sys.exit()
        # Must exit because calling the function back brings up a bug

    elif len(binary_input) > 8:
        print("Only up to 8 bits allowed.")
        sys.exit()
        # Must exit because calling the function back brings up a bug

    for number in binary_input:
        decimal_value = decimal_value * 2 + int(number)
        # Gotta make that numbah a integer
    print("Decimal Value:", + decimal_value)

def decimal_calc():
    """ Receives input in the form
       of a decimal value
       and returns its binary number """
    try:
        decimal_input = int(input("Decimal value: "))
        print("Binary number:", "{0:{fill}8b}".format(decimal_input, fill="0"))
        # It fills up to 8 bits with 0s (if number is under 255).
        # For no-filling, use: "{0:b}".format(number)
    except ValueError:
        print(">>> Only numbers are allowed <<<")
        decimal_calc()

intro_options()
