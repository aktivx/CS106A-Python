from karel.stanfordkarel import *

"""
File: OurSteepleChaseKarel.py
--------------------------------
Karel runs a steeple chase the is 9 avenues long.
Hurdles are of arbitrary height and placement.
"""


def main():
    put_beeper()
    if front_is_clear():
        while front_is_clear():
            move_L_east_north()
            put_beeper()
        turn_around()
        move_to_wall()
        turn_left()
        while not on_beeper():
            move_L_south_east()

        move_to_wall()
        put_beeper()
        turn_right()
        move_to_wall()
        turn_around()


        while on_beeper():
            pick_beeper()
            move_L_east_north()

        turn_right()
        move_to_wall()
        turn_right()

        while not on_beeper():
            if front_is_clear():
                move()






def move_L_south_east():
    if front_is_clear():
        move()
        if not on_beeper():
            turn_left()
            if front_is_clear():
                move()
                turn_right()


def move_L_east_north():
    if front_is_clear():
        move()
        turn_left()
        if front_is_clear():
            move()
            turn_right()




"""
    fill_column_board()
    while front_is_clear():
        move_next_column()
        fill_odd_column_board()
        if front_is_clear():
            move_next_column()
            fill_column_board()
#    move_next_column_down()
"""
# precondition row1 facing east
# post condition row1 facing east
def fill_column_board():
    turn_left()
    put_beeper()

    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()

    turn_around()
    move_to_wall()
    turn_left()

def fill_odd_column_board():
    turn_left()
    if front_is_clear():
        move()
        put_beeper()
        while front_is_clear():
            move()
            if front_is_clear():
                move()
                put_beeper()

    turn_around()
    move_to_wall()
    turn_left()







def move_next_column():
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
