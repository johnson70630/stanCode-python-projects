"""
File: extension4_MidpointKarel.py
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
    while front_is_clear():
        put_all()
    find_mid()


def put_all():
    """
    Pre-condition: Karel is on left of the first street, facing East
    Post-condition: Karel is on the right of the first street
    with beepers, facing East
    """
    put_beeper()
    while front_is_clear():
        if on_beeper():
            move()
            put_beeper()
    go_back()
    turn_right()
    # Karel is facing North
    if front_is_clear():
        move()
        turn_right()
        # Karel is facing East


def go_back():
    """
    Pre-condition: Karel is on the right of a street, facing East
    Post-condition: Karel is on the left of a street, facing East
    """
    turn_around()
    # Karel is facing West
    while front_is_clear():
        move()


def turn_around():
    turn_left()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def find_mid():
    turn_right()
    # Karel is facing East
    while on_beeper():
        if front_is_clear():
            pick_beeper()
            move()
            if not on_beeper():
                turn_around()
                move()
                turn_left()
                move()
        else:
            turn_right()
    while front_is_clear():
        if facing_south():
            move()
        if facing_north():
            turn_around()
            move()
    put_beeper()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
