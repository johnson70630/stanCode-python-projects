"""
File: name_sq.py (extension)
Name: Johnson
----------------------------
This program is an extension of assignment3!
It will ask the user to provide a name, 
and the square pattern of the given name 
will be printed on the console.
"""


def main():
    """
    This program prints a name in a square pattern.
    """
    print("This program prints a name in a square pattern")
    name = input("Name: ")
    for i in range(len(name)):
        print(name[i], end="")
    print("")
    for i in range(len(name)-2):
        print(name[i+1], end="")
        for j in range(len(name)-2):
            print(" ", end="")
        print(name[len(name)-i-2])
    for i in range(len(name)):
        print(name[len(name)-i-1], end="")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
