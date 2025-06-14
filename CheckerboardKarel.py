from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""
def main():
    while left_is_clear():
        check_even_row()
        check_row_and_put_beeper()

def check_row_and_put_beeper():
    face_north()
    if front_is_clear():
        move_safely()
        face_east()
        if beepers_present():
            face_north()
            move_safely()
            face_east()
            check_even_row()
            reset()
        else:
            check_odd_row()
            reset()
            face_north()
            move_safely()
    else:
        face_east()
        if beepers_present():
            check_even_row()
            reset()
        else:
            check_odd_row()
            reset()

def check_odd_row():
    move()
    while front_is_clear():
        safely_put_beeper()
        move_safely()
        move_safely()
    put_beeper()

def reset():
    turn_around()
    move_to_wall()
    turn_around()

def check_even_row():
    put_beeper()
    while front_is_clear():
        move_safely()
        move_safely()
        if front_is_clear():
            safely_put_beeper()
    reset()

def safely_put_beeper():
    if no_beepers_present():
        put_beeper()

def skip_beeper():
    if beepers_present():
        move_safely()

def move_to_wall():
    while front_is_clear():
        move()

def move_safely():
    if front_is_clear():
        move()

def face_north():
    while not_facing_north():
        turn_left()

def turn_around():
    turn_left()
    turn_left()

def face_east():
    while not facing_east():
        turn_left()
# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
