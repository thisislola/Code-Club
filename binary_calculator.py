# Binary Calculator by L. Carthy

import time
import re      # Regular Expressions
import sys     # Exit system

def BinaryCalc():
    """ BinaryCalc received input in the form
    of a binary number (1's and 0's)
    and returns its decimal value."""

    try:
        decimal_value = 0  # Set to 0 to change values
        binary_input = input('Binary number: ')
        if not re.match("[0-1]", binary_input):     # It must match 0 or 1
            print("Only 1s and 0s allowed.")
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

    except SyntaxError:
        # Unnecessary because the input is being controlled, so... will fix
        print("Wow, you actually broke this! Well done.")
        time.sleep(2)
        BinaryCalc()

BinaryCalc()
