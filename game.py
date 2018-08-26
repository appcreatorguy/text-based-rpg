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
UP = ''up, north''
DOWN = ''down, south''
LEFT = ''left, west''
RIGHT = ''right, east''

solved_places = {'a1':False, 'a2':False, 'a3':False, 'a4':False,
                'b1':False, 'b2':False, 'b3':False, 'b4':False, 
                'c1':False, 'c2':False, 'c3':False, 'c4':False, 
                'd1':False, 'd2':False, 'd3':False, 'd4':False,
                }

zonemap = {
    'a1':{
        ZONENAME = "Town Market"
        DESCRIPTION = 'description',
        EXAMINATION = 'examine',
        SOLVED = False,
        UP = '',
        DOWN = 'b1',
        LEFT = '',
        RIGHT = 'a2',
    },
    'a2':{
        ZONENAME = "Town Entrance"
        DESCRIPTION = 'description',
        EXAMINATION = 'examine',
        SOLVED = False,
        UP = ' ',
        DOWN = 'b2',
        LEFT = 'a1',
        RIGHT = 'a3',
    },
    'a3':{
        ZONENAME = "Town Square"
        DESCRIPTION = 'description',
        EXAMINATION = 'examine',
        SOLVED = False,
        UP = ' ',
        DOWN = 'b3',
        LEFT = 'a2',
        RIGHT = 'a4',
    },
    'a4':{
        ZONENAME = "Town Hall"
        DESCRIPTION = 'description',
        EXAMINATION = 'examine',
        SOLVED = False,
        UP = 'up, north',
        DOWN = 'DOWN, south',
        LEFT = 'LEFT, west',
        RIGHT = 'RIGHT, east',
    },
    'b1':{
        ZONENAME = ""
        DESCRIPTION = 'description',
        EXAMINATION = 'examine',
        SOLVED = False,
        UP = 'up, north',
        DOWN = 'DOWN, south',
        LEFT = 'LEFT, west',
        RIGHT = 'RIGHT, east',
    },
    'b2':{
        ZONENAME = 'Home'
        DESCRIPTION = 'This is your home!',
        EXAMINATION = 'Your home looks the same - nothing has changed.',
        SOLVED = False,
        UP = 'up, north',
        DOWN = 'DOWN, south',
        LEFT = 'LEFT, west',
        RIGHT = 'RIGHT, east',
    },
    'b3':{
        ZONENAME = ""
        DESCRIPTION = 'description',
        EXAMINATION = 'examine',
        SOLVED = False,
        UP = 'a2',
        DOWN = 'c2',
        LEFT = 'b1',
        RIGHT = 'b3',
    },
    'b4':{
        ZONENAME = ""
        DESCRIPTION = 'description',
        EXAMINATION = 'examine',
        SOLVED = False,
        UP = 'up, north',
        DOWN = 'DOWN, south',
        LEFT = 'LEFT, west',
        RIGHT = 'RIGHT, east',
    }, 


}