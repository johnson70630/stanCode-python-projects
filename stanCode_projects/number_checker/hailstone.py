"""
File: hailstone.py
Name: Johnson
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""

EXIT = 1  # Sentinel Value


def main():
    print("This program computes Hailstone sequences")
    num = int(input("Enter a number: "))
    step = 0
    while True:
        if num == EXIT:
            break
        elif num % 2 == 1:
            print(str(num) + " is odd, so I make 3n+1: ", end="")
            num = num*3+1
            print(str(num))
        else:
            print(str(num) + " is even, so I take half: ", end="")
            num = int(num/2)
            print(str(num))
        step += 1
    print("It took "+str(step)+" steps to reach 1")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
