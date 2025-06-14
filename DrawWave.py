from karel.stanfordkarel import *


def main():
    draw_waves()


def draw_waves():
    while front_is_clear():
        draw_wave()
        move_safely()
        move_safely()


def move_safely():
    if front_is_clear():
        move()


def draw_wave():
    put_two_beepers_in_row()
    face_north()
    move()
    put_beeper()
    face_south()
    move_to_wall()
    face_east()


def move_to_wall():
    if front_is_clear():
        move()


def put_two_beepers_in_row():
    if no_beepers_present():
        put_beeper()
        move()
        put_beeper()


def face_north():
    while not_facing_north():
        turn_left()


def face_east():
    while not_facing_east():
        turn_left()


def face_south():
    while not_facing_south():
        turn_left()


if __name__ == '__main__':
    run_karel_program()