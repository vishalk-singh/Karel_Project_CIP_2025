from karel.stanfordkarel import *
"""
File: HospitalKarel.py
------------------------
Run the blank programme. 
Each beeper in the represents a pile of supplies. 
Karel's job is to walk along 1st Street and build a new hospital in the places marked by each beeper. 
The new hospital should be centered at the point at which the bit of debris was left, 
which means that the first hospital in the diagram above will be constructed with its left edge along 2nd Avenue, 
since the beeper was originally at 3rd Avenue.
At the end of the run, Karel should be at the east end of 1st street facing East.

Keep in mind the following information about the world:
1. Karel starts facing east at (1, 1) with an infinite number of beepers in its beeper bag.
2. The beepers indicating the positions at which hospitals should be built will be spaced so that 
    there is room to build the hospitals without overlapping or hitting walls.
3. You will not have to build a hospital that starts in either of the last two columns.
4. Karel should not crash into a wall if it builds a hospital that ends in the final corner.

Write the code to implement Hospital Karel. 
Use helper functions. Think, "what are the high-level steps Karel needs to take?" 
and make these steps into helper functions. 
Remember that your program should work for any world that meets the above conditions.
"""


def main():
    while front_is_clear():
        move_to_next_hospital()
        build_hospital()

def build_hospital():
    build_tower()
    move_safely()
    build_tower()

def build_tower():
    build_a_wall()
    move_to_bottom()

def move_to_bottom():
    face_south()
    while front_is_clear():
        move()
    face_east()

def build_a_wall():
    face_north()
    for i in range(3):
        if no_beepers_present():
            put_beeper()
        move_safely()
        put_beeper()
    face_east()

def move_to_next_hospital():
    move_safely()
    while no_beepers_present():
        move_safely()

def face_north():
    while not_facing_north():
        turn_left()

def face_south():
    while not_facing_south():
        turn_left()

def face_east():
    while not_facing_east():
        turn_left()

def move_safely():
    if front_is_clear():
        move()
if __name__ == "__main__":
    run_karel_program()
