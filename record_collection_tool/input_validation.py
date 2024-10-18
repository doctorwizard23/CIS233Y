# Author: Noah McGarry
# Date: 10/12/2024
# !/usr/bin/env python3


def input_int(prompt="Enter an integer: ", gt=None, ge=None, lt=None, le=None):
    """
    Function to prompt for and return a valid integer.
    :param: prompt, string, string to be used as prompt
    :param: gt, float, optional 'greater than' parameter
    :param: ge, float, optional 'greater than or equal to' parameter
    :param: lt, float, optional 'less than' parameter
    :param: le, float, optional 'less than or equal to' parameter
    :return: val, integer, valid integer
    """
    while True:
        try:
            val = int(input(prompt))
            if gt is not None and val <= gt:
                print(F"Value must be greater than {gt}!")
                continue
            elif ge is not None and val < ge:
                print(F"Value must be greater than or equal to {ge}!")
                continue
            elif lt is not None and val >= lt:
                print(F"Value must be less than {lt}!")
                continue
            elif le is not None and val > le:
                print(F"Value must be less than or equal to {le}!")
                continue
            return val
        except ValueError:
            print("Invalid integer.")


def input_float(prompt="Enter a decimal number: ", gt=None, ge=None, lt=None, le=None):
    """
    Function to prompt for and return a valid real(floating point) number
    :param: prompt, string, optional string to use as prompt
    :param: gt, float, optional 'greater than' parameter
    :param: ge, float, optional 'greater than or equal to' parameter
    :param: lt, float, optional 'less than' parameter
    :param: le, float, optional 'less than or equal to' parameter
    :return: val, float, valid real floating point number
    """
    while True:
        try:
            val = float(input(prompt))
            if gt is not None and val <= gt:
                print(F"Value must be greater than {gt}!")
                continue
            elif ge is not None and val < ge:
                print(F"Value must be greater than or equal to {ge}!")
                continue
            elif lt is not None and val >= lt:
                print(F"Value must be less than {lt}!")
                continue
            elif le is not None and val > le:
                print(F"Value must be less than or equal to {le}!")
                continue
            return val
        except ValueError:
            print("Invalid number.")


def input_string(prompt="Please enter a word: ", valid=True):
    """
    Function to prompt for and return a string of alphabetic characters.
    An empty string is invalid input.
    :param valid: boolean validation function
    :param prompt: string Optional string to use as prompt
    :return: string Non-empty string of characters
    """
    while True:
        try:
            string = input(prompt)
            valid = bool(string.isalpha())
            # I tried to utilize lambda validation dozens of different ways, but I couldn't get it to work,
            # so I used this method.
            if string != "" and valid is True:
                return string
            else:
                print("Invalid input (Use only letters).")
        except ValueError:
            print("Invalid entry.")


def y_or_n(prompt="Please enter 'yes' or 'no': "):
    """
    Function to prompt for and return yes or no.
    :param prompt: string, Optional string to use as prompt
    :return yes: string, affirmative response
    :return no: string, negative response
    """
    while True:
        answer = input(prompt).lower()
        if answer in ["y", "yes"]:
            return "Yes"
        elif answer in ["n", "no"]:
            return "No"
        else:
            print("Invalid answer.")


# def select_item(prompt="Please select an option: ", choices=["Yes", "No"]):
#     """
#     Function to prompt for a selection from a provided list and return that selection
#     :param prompt: string, Optional string to use as prompt
#     :param items: list, provided list of selections
#     :return: items [choice - 1], selection from provided list
#     """
#     while True:
#         for i, item in enumerate(items):
#             print(f"{i + 1}. {item}")
#
#         try:
#             choice = int(input(prompt))
#             if 1 <= choice <= len(items):
#                 return items[choice - 1]
#             else:
#                 print("Invalid selection.")
#         except ValueError:
#             print("Invalid input")

def select_item(prompt="Please type yes or no: ", error="Answer must be yes or no!", choices=["Yes", "No"], map=None):
    """
    Function to prompt for a selection from a provided list and return that selection
    :param prompt: string, Optional string to use as prompt
    :param error: string, Optional error message
    :param choices: list, provided list of selections
    :param map: optional map function to apply a function to an iterable
    :return: selection from provided list
    """
    value_dict = {}
    for choice in choices:
        value_dict[choice.lower()] = choice
    if map is not None:
        for key in map:
            value_dict[key.lower()] = map[key]
    while True:
        val = input(prompt).lower()
        if val in value_dict:
            return value_dict[val]
        print(error)

def input_value(prompt="Please enter a value: ", type=""):
    """
    Function to prompt for and return a valid value based on the selected validation.
    :param prompt: string, Optional string to use as prompt
    :param type: selection of function to validate the input
    :return: value of the return of the selected function
    """
    while True:
        if type == "int":
            val = input_int(prompt)
            return val
        elif type == "float":
            val = input_float(prompt)
            return val
        elif type == "str":
            val = input_string(prompt)
            return val
        elif type == "y_or_n":
            val = y_or_n(prompt)
            return val
        elif type == "select_item":
            val = select_item(prompt)
            return val
        else:
            print("Invalid selection.")
