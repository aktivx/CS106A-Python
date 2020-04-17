from karel.stanfordkarel import *


def main():
    # build_hospital()

    while front_is_clear():
        move()
        if beepers_present():
            turn_around()
            move()
            turn_around()
            build_hospital()



    # find_hospital_position()

    # def find_hospital_postion():
    #
    #     while front_is_clear():


def build_hospital_wall():
    turn_left()
    for i in range(3):
        put_beeper()
        move()
    turn_right()

def build_hospital_right_wall():
    build_hospital_wall()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    if front_is_clear():
        move()

def build_hospital_cover():
    move()
    turn_right()
    for i in range(3):
        put_beeper()
        move()
    pick_beeper()
    turn_left()
    move()


def build_hospital():
    build_hospital_wall()
    build_hospital_cover()
    build_hospital_right_wall()

def turn_right():
   for i in range(3):
      turn_left()

def turn_around():
    turn_left()
    turn_left()


if __name__ == "__main__":
    run_karel_program()
