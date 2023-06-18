"""
File: MidpointKarel.py
Name: Johnson
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will find the mid point with a beeper on the first street
    """
    fill_beeper()
    go_back()
    find_mid()


def fill_beeper():
    """
    Pre-condition: Karel is on left of the first street, facing East
    Post-condition: Karel is on the right of the first street, facing East
    and the street had filled with beepers
    """
    while front_is_clear():
        move()
        put_beeper()
    pick_beeper()


def go_back():
    """
    Pre-condition: Karel is on right of the first street, facing East
    Post-condition: Karel is on the left of the street, facing East
    """
    turn_around()
    # Karel is facing West
    while front_is_clear():
        move()
    turn_around()
    # Karel is facing East


def turn_around():
    turn_left()
    turn_left()


def find_mid():
    """
    Pre-condition: Karel is on the left of the street, facing East
    Post-condition: Karel is on the mid point of the street, facing South
    """
    while front_is_clear():
        move()
        if not on_beeper():
            turn_around()
            move()
            if on_beeper():
                pick_beeper()
            else:
                turn_right()
                put_beeper()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #
if __name__ == '__main__':
    execute_karel_task(main)
