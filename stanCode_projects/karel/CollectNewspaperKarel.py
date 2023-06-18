"""
File: CollectNewspaperKarel.py
Name: Johnson
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will pick the newspaper outside the house
    and go back to the start, putting the newspaper down
    """
    go_outside()
    go_back()


def go_outside():
    """
    Pre-condition: Karel is at upper left in the house, facing East
    Post-condition: Karel is outside the house and stand
    on the beeper, facing East
    """
    while front_is_clear():
        move()
    turn_right()
    # Karel is facing South
    move()
    turn_left()
    # Karel is facing East
    move()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def go_back():
    """
    Pre-condition:Karel is outside the house and stand
    on the beeper, facing East
    Post-condition: Karel is at upper left in the house
    with the beeper down, facing East
    """
    pick_beeper()
    turn_around()
    # Karel is facing West
    while front_is_clear():
        move()
    turn_right()
    # Karel is facing North
    move()
    turn_right()
    # Karel is facing East
    put_beeper()


def turn_around():
    turn_left()
    turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
