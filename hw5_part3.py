"""
File:         hw5_part3.py
Author:       Vu Nguyen
Date:         10/16/2020
Section:      31
E-mail:       vnguye12@umbc.edu
Description:  This programs take in the the room dimension and
              the starting position of the robot. The robot will
              move right, down, left, up, in that order. If there's
              an empty ('') then the robot will go to that position
              leaving behind a trail of ascending number starting at 1.
"""
DOT = '.'
TOP_ROW = 0
LEFT_ROW = 0
EMPTY_SPACE = ''


def print_robo_array(room):
    for row in room:
        for x in row:
            if not x:
                print(DOT.ljust(3), end=' ')
            else:
                print(str(x).ljust(3), end=' ')
        print()
    print()


def robo_vac(room, starting_y, starting_x):
    """
    Compute a path through the room for the robot vacuum.

    :param room: a 2d-grid representing the room,
                '' blank strings are open spaces
    :param starting_y: starting row (first index)
    :param starting_x: starting column (second index)
    :return: the updated room with the numbers.
    """
    same_position = 1
    current_step = 1
    can_move = True
    x = starting_x
    y = starting_y
    room[y][x] = current_step

    while can_move:

        # Check to see if the robot can move right
        if (x < len(room[y]) - 1) and (room[y][x + 1] == EMPTY_SPACE):
            current_step += 1
            x += 1
            room[y][x] = current_step

        # Check to see if the robot can move down
        elif (y < len(room) - 1) and (room[y + 1][x] == EMPTY_SPACE):
            current_step += 1
            y += 1
            room[y][x] = current_step

        # Check to see if the robot can move left
        elif (x > LEFT_ROW) and (room[y][x - 1] == EMPTY_SPACE):
            current_step += 1
            x -= 1
            room[y][x] = current_step

        # Check to see if the robot can move up
        elif (y > TOP_ROW) and (room[y - 1][x] == EMPTY_SPACE):
            current_step += 1
            y -= 1
            room[y][x] = current_step

        # Check to see if the robot is trap
        else:
            same_position = current_step

        # Check to make sure that the robot moved.
        if same_position == current_step:
            can_move = False

    return room


if __name__ == '__main__':
    my_room = [['' for _ in range(6)] for _ in range(6)]
    print_robo_array(robo_vac(my_room, 0, 0))
    my_room_with_obstacles = [['' for _ in range(6)] for _ in range(6)]

    for i in range(3, 5):
        for j in range(3, 5):
            my_room_with_obstacles[i][j] = 'x'
    print_robo_array(robo_vac(my_room_with_obstacles, 0, 0))

    my_smaller_room = [['', '', ''], ['', 'x', 'x'], ['', '', 'x']]
    print_robo_array(robo_vac(my_smaller_room, 0, 0))
    my_smaller_room = [['', '', ''], ['', 'x', 'x'], ['', '', 'x']]
    print_robo_array(robo_vac(my_smaller_room, 0, 2))

    another_room = [
        ['', 'x', '', '', '', '', '', ''],
        ['', 'x', 'x', '', 'x', '', 'x', ''],
        ['', 'x', '', '', 'x', 'x', '', ''],
        ['', '', '', '', 'x', '', 'x', ''],
        ['', '', 'x', '', 'x', '', 'x', ''],
        ['', '', 'x', '', 'x', '', 'x', ''],
        ['', '', '', '', 'x', '', 'x', ''],
        ['', '', '', '', '', '', '', '']
    ]
    print_robo_array(robo_vac(another_room, 0, 0))

