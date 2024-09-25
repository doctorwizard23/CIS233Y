# Author: Noah McGarry
# Date: 9/24/2024
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
            if ge is not None and val < ge:
                print(F"Value must be greater than or equal to {ge}!")
                continue
            if lt is not None and val >= lt:
                print(F"Value must be less than {lt}!")
                continue
            if le is not None and val > le:
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
            if ge is not None and val < ge:
                print(F"Value must be greater than or equal to {ge}!")
                continue
            if lt is not None and val >= lt:
                print(F"Value must be less than {lt}!")
                continue
            if le is not None and val > le:
                print(F"Value must be less than or equal to {le}!")
                continue
            return val
        except ValueError:
            print("Invalid number.")
