"""
File: extension2_number_checker.py
Name: Johnson
------------------------
This program asks our user for input and checks if the input is a
perfect number、deficient number or an abundant number.

A number is said to be perfect if it is equal to the sum of all its
factors (for obvious reasons the list of factors being considered does
not include the number itself).

A number is considered to be abundant if the sum of its factors
(aside from the number) is greater than the number itself.

And a number is said to be deficient if it is bigger than the sum of all its
factors(aside from the number itself).

The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
    print("Welcome to the number checker!")
    while True:
        n = int(input("n: "))
        if n == EXIT:
            print("Have a good one!")
            break
        else:
            x = 1
            total = 0
            while True:
                if n == x:
                    break
                elif n % x == 0:
                    total += x
                    x += 1
                else:
                    x += 1
        if total > n:
            print(str(n)+" is a abundant number")
        elif total < n:
            print(str(n)+" is a deficient number")
        else:
            print(str(n)+" is a perfect number")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
