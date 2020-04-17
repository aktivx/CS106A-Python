from karel.stanfordkarel import *

"""
File: OurSteepleChaseKarel.py
--------------------------------
Karel runs a steeple chase the is 9 avenues long.
Hurdles are of arbitrary height and placement.
"""


def main():
    move_to_nespaper()
    pick_beeper()
    turn_around()
    return_home()

def move_to_nespaper():
    turn_right()
    move()
    turn_left()
    for i in range(3):
        move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()

def return_home():
    for i in range(3):
        move()
    turn_right()
    move()
    turn_right()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
