"""
File: rocket.py
Name: Johnson
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 3


def main():
    """
    This program prints a rocket.
    """
    rocket_head()
    rocket_belt()
    rocket_upper()
    rocket_lower()
    rocket_belt()
    rocket_head()


def rocket_head():
    for i in range(SIZE):
        for j in range(SIZE-i):
            print(" ", end="")
        for j in range(i+1):
            print("/", end="")
        for j in range(i+1):
            print("\\", end="")
        print("")


def rocket_belt():
    print("+", end="")
    for i in range(2):
        for j in range(SIZE):
            print("=", end="")
    print("+", end="")
    print("")


def rocket_upper():
    for i in range(SIZE):
        print("|", end="")
        for j in range(SIZE-i-1):
            print(".", end="")
        for j in range(i+1):
            print("/", end="")
            print("\\", end="")
        for j in range(SIZE-i-1):
            print(".", end="")
        print("|", end="")
        print("")


def rocket_lower():
    for i in range(SIZE):
        print("|", end="")
        for j in range(i):
            print(".", end="")
        for j in range(SIZE-i):
            print("\\", end="")
            print("/", end="")
        for j in range(i):
            print(".", end="")
        print("|", end="")
        print("")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
