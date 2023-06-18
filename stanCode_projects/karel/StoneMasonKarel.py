"""
File: StoneMasonKarel.py
Name: Johnson
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will fill all pillars with beepers
    """
    while front_is_clear():
        fill_the_pillar()
        another_pillar()
    fill_the_pillar()


def fill_the_pillar():
    """
    Pre-condition: karel is below the pillar, facing East
    Post-condition: Karel is below the pillar, facing East,
    and the pillar had filled with beepers
    """
    turn_left()
    # Karel is facing North
    if not on_beeper():
        put_beeper()
    while front_is_clear():
        move()
        if not on_beeper():
            put_beeper()
    go_back()


def go_back():
    """
    Pre-condition: Karel is at the top of the pillar, facing North
    Post-condition: Karel is below the pillar, facing East
    """
    turn_around()
    # Karel is facing South
    while front_is_clear():
        move()
    turn_left()
    # Karel is facing East


def turn_around():
    turn_left()
    turn_left()


def another_pillar():
    """
    Pre-condition: Karel is below the pillar, facing East
    Post-condition: Karel moved to the next pillar, facing East
    """
    for i in range(4):
        move()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
