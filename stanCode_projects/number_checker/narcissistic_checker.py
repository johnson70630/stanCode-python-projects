"""
File: extension4_narcissistic_checker.py
Name: Johnson
------------------------
This program asks our user for input and checks if the input is a
narcissistic number or not.

A positive integer is called a narcissistic number if it
is equal to the sum of its own digits each raised to the
power of the number of digits.

Example: 153 is narcissistic because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
Note that by this definition all single digit numbers are narcissistic.

Students are recommended to use // and % to complete this program.

The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
    print("Welcome to the narcissistic number checker!")
    while True:
        n = int(input("n: "))
        if n == EXIT:
            print("Have a good one!")
            break
        else:
            a = 10
            b = 1
            while n > a:
                b += 1
                a *= 10
            c = 10
            d = n
            total = 0
            while d > c:
                total += (d % c)**b
                d = (d-(d % c))/10
            total += d**b
            if total == n:
                print(str(n)+" is a narcissistic number")
            else:
                print(str(n)+" is not a narcissistic number")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
