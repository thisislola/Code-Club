# Temperature Calculator by L. Carthy

import time

def intro_options():
    """ Takes the option and returns the fuction
    that correlates """

    option = int(input("1 for Fahrenheit to Celsius \n"
                        "2 for Celcius to Fahrenheit \n"
                        "3 for Fahrenheit to Kelvin: "))
    if option == 1:
        ftoc_calc()
    elif option == 2:
        ctof_calc()
    elif option == 3:
        ftk_calc()
    else:
        print("That is not an option. Try again.")
        time.sleep(2)
        intro_options()

def ftoc_calc():
    """Calculates from Fahrenheit to Celsius.
    Returns the value of the calculation """

    try:
        ftc_input = int(input("Enter the Fahrenheit value: "))
        ftc_conversion = (ftc_input - 32) * 5/9
        print("Your answer in Celsius is: ", ftc_conversion)
    except ValueError:
        print("Error: Your input is not a number. Try again.")
        time.sleep(2)
        ftoc_calc()

def ctof_calc():
    """Calculates from Celsius to Fahrenheit.
        Returns the value of the calculation """

    try:
        ctf_input = int(input("Enter the Celsius value: "))
        ctf_conversion = ctf_input * 9/5 + 32
        print("Your answer in Fahrenheit is: ", ctf_conversion)
    except ValueError:
        print("Error: Your input is not a number. Try again.")
        time.sleep(2)
        ftoc_calc()

def ftk_calc():
    """Calculates from Fahrenheit to Kelvin.
        Returns the value of the calculation """

    try:
        ftc_input = int(input("Enter the Fahrenheit value: "))
        ftc_conversion = (ftc_input + 459.67) * 5/9
        print("Your answer in Kelvin is: ", ftc_conversion)
    except ValueError:
        print("Error: Your input is not a number. Try again.")
        time.sleep(2)
        ftoc_calc()

intro_options()
