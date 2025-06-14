from karel.stanfordkarel import *
"""
Program: Democrary Karel
Karel traverses a ballot from left to right, removing the 
"hanging chads".
"""


def main():
    while front_is_clear():
        process_column()
        move()
    # handles fencepost problem for last column
    process_column()


def process_column():
    """
    Clears chad from the current column, if any.
    Pre-condition: Karel is standing in the center of a column,
        facing east.
    Post-condition: Karel is back in the same place/orientation
        and chad (if any) has been cleared.
    """
    if no_beepers_present():
        remove_chad()


def remove_chad():
    """
    Clears chad from the current column.
    Pre-condition: Karel is standing in the center of a
        column to be cleared, facing east.
    Postcondition: Karel is standing in the same place/
        orientation and the column has been cleared.
    """
    # clean upper corner
    turn_left()
    remove_beepers_front()
    turn_around()
    # clean lower corner
    remove_beepers_front()
    turn_left()


def remove_beepers_front():
    """
    Clears chad from whichever corner Karel is facing.
    Pre-condition: Karel is facing a corner to be cleared of
        the chad (beepers).
    Post-condition: Karel is in the same location/orientation,
        but the chad has been cleared from the corner Karel
        is facing.
    """
    move()
    while beepers_present():
        pick_beeper()
    back_up()


def back_up():
    turn_around()
    move()
    turn_around()


def turn_around():
    turn_left()
    turn_left()

if __name__ == "__main__":
    run_karel_program()
