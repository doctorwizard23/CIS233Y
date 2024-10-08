# Author: Noah McGarry
# Date: 10/7/2024
# !/usr/bin/env python3


from input_validation import input_int, input_float, input_string, y_or_n, select_item, input_value


hats = ["Cowboy Hat", "Fedora", "Top Hat", "Sombrero"]


def main():
    print("Welcome to the selection game!")
    print(input_value("Are you ready to play? :", type="y_or_n"),
          "? Either way, here we go!")
    print(select_item("Select your favourite hat (select by number): ", hats),
        "is a good hat.")
    print(input_string("What is your favourite food (Use only letters of the alphabet): "),
        "is delicious.")
    # I had a ton of trouble getting the input_string validation to work using the lambda function,
    # so I used a different method inside the function
    print(y_or_n("Are you excited to make lots of selections?: "),
        "is the correct response!")
    print(input_int("Please enter an integer: "),
        "is a valid integer.")
    print(input_float("Please enter a decimal number: "),
        "is a valid decimal number.")
    print(input_int("Please enter an integer between 10 and 77: ", le=77, ge=10),
        "is within the range of 10 to 77.")
    print(input_int("Please enter a integer greater than or equal to 7 and less than 45: ", ge=7, lt=45),
        "is within the range of 7 to 45.")
    print(input_float("Please enter a decimal number between 2.7 and 22.3 inclusive: ", ge=2.7, le=22.3),
        "is within the range of 2.7 to 22.3")
    print(input_float("Enter a positive decimal number: ", ge=0.0),
        "is a positive decimal number.")
    print(input_int("Enter a negative integer: ", lt=0),
        "is a negative integer.")
    print("Thank you for playing.")


if __name__ == "__main__":
    main()