# Author: Noah McGarry
# Date: 10/18/2024
# !/usr/bin/env python3




from VinylRecord import VinylRecord
from input_validation import select_item


class ConsoleUI:
    CHOICES = ["1", "2"]


    @classmethod
    def init(cls):
        cls.__all_records = VinylRecord.get_records()

    @classmethod
    def list_records(cls):
        for record in cls.__all_records:
            print()
            print(record.get_key(), " - ", record, sep="")

    @staticmethod
    def print_menu():
        print()
        print("Please select a number from the list below:")
        print()
        print(
            " 1. List all records\n",
            "2. Exit"
        )
        print()


    @classmethod
    def run(cls):
        while True:
            cls.print_menu()
            choice = select_item("Please select an item: ", "Invalid selection." ,cls.CHOICES)
            if choice == "1":
                cls.list_records()
            elif choice == "2":
                break

        print()
        print("Thank you for using the Vinyl Record Collection Tool!")

if __name__ == '__main__':
    ConsoleUI.init()
    ConsoleUI.run()
