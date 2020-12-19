"""
File:         hw5_part4.py
Author:       Vu Nguyen
Date:         10/16/2020
Section:      31
E-mail:       vnguye12@umbc.edu
Description:  This battle to the death programs let user
              choose two creature from a file, and have
              both of them fight each others. Very Cruel.
"""


def read_creature_file(creature_file_name):
    """
    :param creature_file_name: a json file with creature stats.
    :return: a python dictionary of creatures.
    """
    import json
    try:
        with open(creature_file_name) as f:
            return json.loads(f.read())
    except OSError:
        print('Unable to open the file, is it in the right place? ')

    return {}


def fight_creatures(first_creature, second_creature):

    # adding alive key and value into both creatures attribute.
    first_creature['alive'] = True
    second_creature['alive'] = True

    both_no_first_strike = not(first_creature['first_strike'] and second_creature['first_strike'])

    # This checks if both creature have first strike no both doesn't have first strike.
    if (first_creature['first_strike'] and second_creature['first_strike']) or both_no_first_strike:

        # This check the first creature than second
        if first_creature['life'] <= second_creature['attack']:

            # If both the first and the second creatures have more attack than the other monsters health, both die.
            if second_creature['life'] <= first_creature['attack']:
                first_creature['alive'] = False
                second_creature['alive'] = False

            # Comparing both attacks, the first creature have less health but the second have more health, first die.
            else:
                first_creature['alive'] = False

        # This check the second creature than first
        else:

            # If both the first and the second creatures have more attack than the other monsters health, both die.
            if first_creature['life'] <= second_creature['attack']:
                first_creature['alive'] = False
                second_creature['alive'] = False

            # Comparing both attacks, the second creature have less health but the first have more health, second die.
            else:
                second_creature['alive'] = False

    # This check if the first_creature have first strike
    elif first_creature['first_strike']:

        # first_creature attack first.
        if second_creature['life'] <= first_creature['attack']:
            second_creature['alive'] = False

    # This check if the second_creature have the first strike
    elif second_creature['first_strike']:

        # second_creature attack first.
        if first_creature['life'] <= second_creature['attack']:
            first_creature['alive'] = False


if __name__ == '__main__':
    creatures = read_creature_file(input('What creature file do you want to load? '))
    if creatures:
        while input('Fight again?').strip().lower() in ['yes', 'y']:
            first_creature_name = input('What is the first creature? ')
            second_creature_name = input('What is the second creature? ')
            if first_creature_name in creatures and second_creature_name in creatures:
                first_creature = creatures[first_creature_name]
                second_creature = creatures[second_creature_name]

                fight_creatures(first_creature, second_creature)

                # hint, are these magic values? hmm... should you do this in your own code?
                print(first_creature_name, first_creature['attack'], first_creature['life'], first_creature['alive'])
                print(second_creature_name, second_creature['attack'], second_creature['life'], second_creature['alive'])

                if first_creature['alive']:
                    print(first_creature_name, 'has survived the fight. ')
                else:
                    print(first_creature_name, 'has died in the fight. ')
                if second_creature['alive']:
                    print(second_creature_name, 'has survived the fight. ')
                else:
                    print(second_creature_name, 'has died in the fight. ')
            else:
                print('One of the creatures wasn\'t in the list of creatures')



