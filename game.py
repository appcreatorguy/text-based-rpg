# Python Text RPG
# Manas Mengle

import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

##### Player Setup #####
class player:
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 'start'
my_player = player()

##### Title Screen #####
def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        start_game() # placeholder until written
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command.")
        option = input("> ")
        if option.lower() == ("play"):
            start_game() # placeholder until written
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()

def title_screen():
    os.system('clear')
    print('|  \/  |(_)                        | |                  | |            | |')
    print('| .  . | _  ___   ___  _ __    ___ | |__    __ _  _ __  | |_   ___   __| |')
    print('| |\/| || |/ __| / _ \|  _ \  / __||  _ \  / _  ||  _ \ | __| / _ \ / _  |')
    print('| |  | || |\__ \|  __/| | | || (__ | | | || (_| || | | || |_ |  __/| (_| |')
    print('\_|  |_/|_||___/ \___||_| |_| \___||_| |_| \__,_||_| |_| \__| \___| \__,_|')
    print('')
    print('-Play-  -Help-  -Quit-')
    title_screen_selections()

def help_menu():
    print('- Use up, down, left, right to move')
    print('- Type your commands to do them')
    print('- Use "Look" to inspect something')
    print('- Good Luck and have fun!')
    title_screen_selections()





##### Game Functionality #####
def start_game():
    pass



##### Map #####
"""
a1 a2... # PLAYER STARTS AT b2
-------------
|  |  |  |  | a4
------------- 
|  |  |  |  | b4 ...
-------------
|  |  |  |  |
-------------
|  |  |  |  |
-------------
"""

ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up, north'
DOWN = 'down, south'
LEFT = 'left, west'
RIGHT = 'right, east'


solved_places = {'a1':False, 'a2':False, 'a3':False, 'a4':False,
                'b1':False, 'b2':False, 'b3':False, 'b4':False, 
                'c1':False, 'c2':False, 'c3':False, 'c4':False, 
                'd1':False, 'd2':False, 'd3':False, 'd4':False,
                }

zonemap = {
    'a1': {
        ZONENAME: "Town Market",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: 'b1',
        LEFT: '',
        RIGHT: 'a2',
    },

    'a2': {
        ZONENAME: "Town Entrance",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: 'b2',
        LEFT: 'a1',
        RIGHT: 'a3',
    },

    'a3': {
        ZONENAME: "Town Square",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: 'b3',
        LEFT: 'a2',
        RIGHT: 'a4',
    },

    'a4': {
        ZONENAME: "Town Hall",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: 'b4',
        LEFT: 'a3',
        RIGHT: '',
    },

    'b1': {
        ZONENAME: "Dungeon",
        DESCRIPTION: 'A glowing something in the distance... What could it be?',
        EXAMINATION: "It's a dungeon full of monsters! The door closes behind you. No escape...",
        SOLVED: False,
        UP: 'a1',
        DOWN: 'c1',
        LEFT: '',
        RIGHT: 'b2',
    },

    'b2': {
        ZONENAME: "Home",
        DESCRIPTION: 'This is your home.',
        EXAMINATION: 'Your Home looks the same - nothing has changed.',
        SOLVED: False,
        UP: 'a2',
        DOWN: 'c2',
        LEFT: 'b1',
        RIGHT: 'b3',
    },

    'b3': {
        ZONENAME: "Forest",
        DESCRIPTION: 'This is area, lonely and full of trees, is part of a forest.',
        EXAMINATION: 'You notice a few mushrooms growing. You decide against eating them',
        SOLVED: False,
        UP: 'a2',
        DOWN: 'c3',
        LEFT: 'b2',
        RIGHT: 'b4',
    },

    'b4': {
        ZONENAME: "Treasure Chest",
        DESCRIPTION: 'A glowing something in the distance... What could it be?',
        EXAMINATION: 'Upon further inspection, it turns out to be a treasure chest! You open it up.',
        SOLVED: False,
        UP: 'a4',
        DOWN: 'c4',
        LEFT: 'b3',
        RIGHT: '',
    },

    'c1': {
        ZONENAME: "Treasure Chest",
        DESCRIPTION: 'A glowing something in the distance... What could it be?',
        EXAMINATION: 'Upon further inspection, it turns out to be a treasure chest! You open it up.',
        SOLVED: False,
        UP: 'b1',
        DOWN: 'd1',
        LEFT: '',
        RIGHT: 'c2',
    },

    'c2': {
        ZONENAME: "Forest",
        DESCRIPTION: 'This is area, lonely and full of trees, is part of a forest.',
        EXAMINATION: 'You notice some heather growing. You decide to take a rest on it for a while',
        SOLVED: False,
        UP: 'b2',
        DOWN: 'd2',
        LEFT: 'c1',
        RIGHT: 'c3',
    },

    'c3': {
        ZONENAME: "Pathway",
        DESCRIPTION: 'Nothing but grass and dirt until the next place',
        EXAMINATION: 'The shouty guy just said, NOTHING HERE!',
        SOLVED: False,
        UP: 'b3',
        DOWN: 'd3',
        LEFT: 'c2',
        RIGHT: 'c4',
    },

    'c4': {
        ZONENAME: "Dungeon",
        DESCRIPTION: 'A glowing something in the distance... What could it be?',
        EXAMINATION: "It's a dungeon full of monsters! The door closes behind you. No escape...",
        SOLVED: False,
        UP: 'b4',
        DOWN: 'd4',
        LEFT: 'c3',
        RIGHT: '',
    },

    'd1': {
        ZONENAME: "Dungeon",
        DESCRIPTION: 'A glowing something in the distance... What could it be?',
        EXAMINATION: "It's a dungeon full of monsters! The door closes behind you. No escape...",
        SOLVED: False,
        UP: 'c1',
        DOWN: '',
        LEFT: '',
        RIGHT: 'd2',
    },

    'd2': {
        ZONENAME: "Forest",
        DESCRIPTION: 'This is area, lonely and full of trees, is part of a forest.',
        EXAMINATION: 'You notice some plants growing.',
        SOLVED: False,
        UP: 'c2',
        DOWN: '',
        LEFT: 'd1',
        RIGHT: 'd3',
    },

    'd3': {
        ZONENAME: "Pathway",
        DESCRIPTION: 'Nothing but grass and dirt until the next place',
        EXAMINATION: 'Really?',
        SOLVED: False,
        UP: 'up, north',
        DOWN: 'down, south',
        LEFT: 'left, west',
        RIGHT: 'right, east',
    },

    'd4': {
        ZONENAME: "Finish",
        DESCRIPTION: 'Finally, the end.',
        EXAMINATION: "Aren't you gone yet?",
        SOLVED: False,
        UP: 'c4',
        DOWN: '',
        LEFT: 'd3',
        RIGHT: '',
    },
        
}