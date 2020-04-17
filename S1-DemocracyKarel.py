from karel.stanfordkarel import *


def main():



    while front_is_clear():
        if beepers_present():
            move()
        else:
            clear_hanging_chad()
        move()

def clear_hanging_chad():
    turn_left()
    move()
    while beepers_present():
        pick_beeper()
    turn_around()
    move()
    move()
    while beepers_present():
        pick_beeper()
    turn_around()
    move()
    turn_right()





def turn_right():
   for i in range(3):
      turn_left()

def turn_around():
    turn_left()
    turn_left()


if __name__ == "__main__":
    run_karel_program()
