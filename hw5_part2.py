"""
File:         hw5_part2.py
Author:       Vu Nguyen
Date:         10/16/2020
Section:      31
E-mail:       vnguye12@umbc.edu
Description:  This programs compute a list of numbers and display
              them in a pascal format.
"""


def pascal_level(a_list):
    new_list = [1]

    # This condition checks if there are at least two number in the a_list
    if len(a_list) > len(new_list):

        # This loop adds the first and next number together and append it to the new_list
        for index in range(len(a_list) - 1):
            temporary_num = a_list[index] + a_list[index + 1]
            new_list.append(temporary_num)

    new_list.append(1)
    return new_list


if __name__ == '__main__':
    next_line = [1]
    for i in range(10):
        print(next_line)
        next_line = pascal_level(next_line)

    print(pascal_level([1, 2, 3, 4, 5]))
    print(pascal_level([1, 1, 2, 3, 5, 8]))
    print(pascal_level([1, 1, 2, 3, 5, 8, 13, 1]))
