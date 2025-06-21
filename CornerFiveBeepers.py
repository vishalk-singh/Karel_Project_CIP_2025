# File: CornerFiveBeepers.py
# -----------------------------
# Pick five beepers in each corner.
# End at bottom left corner facing east.

from karel.stanfordkarel import *


def main():
    while not facing_south():
        collect_all_beepers()
        move_to_wall()
        turn_left()
    collect_all_beepers()
    move_to_wall()
    turn_left()

def collect_all_beepers():
    while beepers_present():
        if beepers_present():
            pick_beeper()


def move_to_wall():
    while front_is_clear():
        move()


if __name__ == "__main__":
    run_karel_program()
