"""
File: extension2_MidpointKarel.py
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
    find_the_end()
    find_mid()


def find_the_end():
    """
    Pre-condition: Karel is on left of the first street, facing East
    Post-condition: Karel is on the right of the first street
     with beepers, facing East
    """
    put_beeper()
    while front_is_clear():
        if on_beeper():
            pick_beeper()
            move()
            put_beeper()
            turn_around()
            # Karel is facing West
            move()
            turn_around()
            # Karel is facing East
        else:
            move()
            put_beeper()


def turn_around():
    turn_left()
    turn_left()


def find_mid():
    """
    Pre-condition: Karel is on the right of the first street
    with beepers, facing East
    Post-condition: Karel is on the mid point of the street
    with a beeper, facing South
    """
    turn_around()
    # Karel is facing West
    while front_is_clear():
        if on_beeper():
            pick_beeper()
            move()
            put_beeper()
            turn_around()
            # Karel is facing East
            move()
            turn_around()
            # Karel is facing West
        else:
            move()
            if on_beeper():
                pick_beeper()
                if on_beeper():
                    pick_beeper()
                else:
                    turn_around()
                    # Karel is facing East
                    move()
                    turn_right()
                    # Karel is facing South
                    put_beeper()
            else:
                turn_around()
                # Karel is facing East
                move()
                turn_right()
                # Karel is facing South
                put_beeper()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #
if __name__ == '__main__':
    execute_karel_task(main)
