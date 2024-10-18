# Author: Noah McGarry
# Date: 10/12/2024
# !/usr/bin/env python3

# I am clearly having issues with the selection function, but I cant seem to figure it out

from VinylRecord import VinylRecord
from input_validation import select_item


class ConsoleUI:
    CHOICES = ["List all records", "Exit"]


    @classmethod
    def init(cls):
        cls.__all_records = VinylRecord.get_records()

    @classmethod
    def list_records(cls):
        for record in cls.__all_records:
            print(record.get_key())

    @staticmethod
    def print_menu():
        print("Please select an option from the list below:")


    @classmethod
    def run(cls):
        while True:
            cls.print_menu()
            choice = select_item("Please select an item: ", cls.CHOICES)
            if choice == 1:
                cls.list_records()
            elif choice == 2:
                break
            print()

        print("Thank you for using the Vinyl Record Collection Tool!")

if __name__ == '__main__':
    ConsoleUI.init()
    ConsoleUI.run()
