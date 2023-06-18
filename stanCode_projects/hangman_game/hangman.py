"""
File: hangman.py
Name: johnson
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program is a hangman game.
    """
    r = random_word()
    dash = ""
    for i in range(len(r)):
        dash += "-"
    n = N_TURNS
    ans = ""
    print("The word looks like " + dash)
    print("You have " + str(n) + " wrong guesses left.")
    while True:
        g = input("Your guess: ")
        if not g.isalpha():
            print("Illegal format")
        elif len(g) > 1:
            print("Illegal format")
        else:
            g = g.upper()
            if g in r:
                print("You are correct!")
                if g not in ans:
                    ans += g
                dash = ""
                for i in range(len(r)):
                    for j in range(len(ans)):
                        if ans[j] == r[i]:
                            dash += ans[j]
                    if len(dash) < i+1:
                        dash += "_"
                if dash == r:
                    print("You Win!")
                    print("The word was " + r)
                    break
                else:
                    print("The word looks like " + dash)
                    print("You have " + str(n) + " wrong guesses left.")
            else:
                print("There is no " + g + "'s in the word.")
                n -= 1
                if n == 0:
                    print("You are completely hung : (")
                    print("The word was: " + r)
                    break
                else:
                    print("The word looks like " + dash)
                    print("You have " + str(n) + " wrong guesses left.")


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
