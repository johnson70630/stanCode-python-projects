"""
File: CheckerboardKarel.py
Name: Johnson
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will fill the world as a checkerboard with beepers
    """
    while facing_east():
        fill_odd_street()
        go_back()
        next_street()
        fill_even_street()
        go_back()
        next_street()


def fill_odd_street():
    """
    Pre-condition: Karel is on the left of an odd street, facing East
    Post-condition: Karel is on the right of an odd street, facing East,
    with the street filled with beepers as a checkerboard
    """
    put_beeper()
    while front_is_clear():
        if on_beeper():
            move()
            if front_is_clear():
                move()
                put_beeper()


def go_back():
    """
    Pre-condition: Karel is on the right of a street, facing East
    Post-condition: Karel is on the left of a street, facing East
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


def next_street():
    """
    Pre-condition: Karel is on the left of a street, facing East
    Post-condition: Karel is on the left of the next street, facing East
    """
    turn_left()
    # Karel is facing North
    if front_is_clear():
        move()
        turn_right()
        # Karel is facing East


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def fill_even_street():
    """
    Pre-condition: Karel is on the left of a even street, facing East
    Post-condition: Karel is on the right of a street, facing East,
    with the street filled with beepers as a checkerboard
    """
    while front_is_clear():
        if not on_beeper():
            move()
            put_beeper()
            if front_is_clear():
                move()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
