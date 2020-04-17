from karel.stanfordkarel import *

"""
File: OurSteepleChaseKarel.py
--------------------------------
Karel runs a steeple chase the is 9 avenues long.
Hurdles are of arbitrary height and placement.
"""


def main():

    fill_column()
    while front_is_clear():
        move_next_column()
        fill_column()

def move_next_column():
    for i in range(4):
        if front_is_clear():
            move()


def fill_column():
#    turn_north()
    turn_left()
    repair_cell()
    while front_is_clear():
        move()
        repair_cell()
    turn_around()
    move_to_wall()
    turn_left()


def turn_north():
    while not facing_north():
        turn_left()



def repair_cell():
    if not on_beeper():
        put_beeper()

def move_to_wall():
    while front_is_clear():
        move()

def paint_building():
    for i in range(2):
        paint_building_side()
        turn_left()
        move()
    paint_building_side()
    turn_right()

def paint_building_side():
    while left_is_blocked():
        put_beeper()
        if front_is_clear():
            move()





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
