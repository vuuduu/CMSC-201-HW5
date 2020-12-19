import json

if __name__ == '__main__':
    file_name = input('What name do you want to use for the json file? ')
    with open(file_name, 'w') as write_json_file:
        creatures = {}
        while input('New Creature?').strip().lower() in ['yes', 'y']:
            name_of_creature = input('What is the name of the creature? ')
            creatures[name_of_creature] = {}
            creatures[name_of_creature]['attack'] = int(input('What is the attack strength of the creature? '))
            creatures[name_of_creature]['life'] = int(input('What is the life of the creature? '))
            first_strike = input('Does the creature have first strike? ')
            if first_strike.strip().lower() in ['yes', 'y']:
                creatures[name_of_creature]['first_strike'] = True
            else:
                creatures[name_of_creature]['first_strike'] = False

        write_json_file.write(json.dumps(creatures, indent='\t'))