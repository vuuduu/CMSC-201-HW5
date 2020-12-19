"""
File:         hw5_part5.py
Author:       Vu Nguyen
Date:         10/16/2020
Section:      31
E-mail:       vnguye12@umbc.edu
Description:  This programs generate a random list of number and
              the length of that list is based on the user. Then
              it takes that random list and sorted backward from
              biggest to smallest.
"""
import sys
from random import randint, seed

if len(sys.argv) >= 2:
    seed(sys.argv[1])

STOP_PARAM = 'STOP'
MAX_INT = 100


def swap(a_list, first_position, second_position):

    # store the first value in the place_holder_num while replacing the first value with the second value.
    place_holder_num = a_list[first_position]
    a_list[first_position] = a_list[second_position]
    a_list[second_position] = place_holder_num


def find_max_index_after(i, a_list):
    max_value = a_list[i]

    # Check for the last index of the list.
    if i != len(a_list) - 1:

        # This loop goes through each value and find the biggest index that have max value
        for index in range(i + 1, len(a_list)):
            if a_list[index] > max_value:
                max_value = a_list[index]
                i = index

    return i


def reverse_selection_sort(a_list):

    for index in range(len(a_list)):
        max_index = find_max_index_after(index, a_list)
        swap(a_list, index, max_index)

    return a_list


if __name__ == '__main__':
    length_or_stop = input('What length of list do you want to sort? (or STOP to end) ')
    while length_or_stop != STOP_PARAM:
        try:
            the_list = [randint(0, MAX_INT) for _ in range(int(length_or_stop))]
            print('The list is: ', the_list)
            print('The reverse sort is: ', reverse_selection_sort(the_list))
        except ValueError:
            print('You entered a non-STOP, non-integer, try again. ')
        length_or_stop = input('What length of list do you want to sort? (or STOP to end) ')

