from karel.stanfordkarel import *

"""
File: MoveFiveKarel.py
----------------------------
Karel completes a puzzle by:
1. Karel move farward 5 times.
2. Put Beepers in the bottom row.
3. Then move till the end of the puzzle.
4. Define a new function move_to_wall after putting 5 beepers for move till the end of the puzzle.
"""
def main():
    put_five_beepers_in_row()
    move_to_wall()

def put_five_beepers_in_row():
    for i in range(5):
        if no_beepers_present():
            put_beeper()
        move()

def move_to_wall():
    while front_is_clear():
        move()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
