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
        self.hp = 100
        self.mp = 100
        self.status_effects = []
        self.location = 'b2'
        self.items = []
my_player = player()

##### Title Screen #####
def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        start_game() # placeholder until written
    elif option.lower() == ("help"):
        help_menu('title')
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command.")
        option = input("> ")
        if option.lower() == ("play"):
            start_game() # placeholder until written
        elif option.lower() == ("help"):
            help_menu('title')
        elif option.lower() == ("quit"):
            sys.exit()

def title_screen():
    os.system('clear')
    print(' __  __  _                          _                    _              _')
    print('|  \/  |(_)                        | |                  | |            | |')
    print('| .  . | _  ___   ___  _ __    ___ | |__    __ _  _ __  | |_   ___   __| |')
    print('| |\/| || |/ __| / _ \|  _ \  / __||  _ \  / _  ||  _ \ | __| / _ \ / _  |')
    print('| |  | || |\__ \|  __/| | | || (__ | | | || (_| || | | || |_ |  __/| (_| |')
    print('\_|  |_/|_||___/ \___||_| |_| \___||_| |_| \__,_||_| |_| \__| \___| \__,_|')
    print('')
    print('-Play-  -Help-  -Quit-')
    title_screen_selections()

def help_menu(title_or_game):
    print('- Use up, down, left, right to move')
    print('- Type your commands to do them')
    print('- Use "Look" to inspect something')
    print('- Good Luck and have fun!')
    if title_or_game == 'title':
        title_screen_selections()
    elif title_or_game == 'game':
        prompt()

##### Game Functionality #####
def start_game():
    prompt()







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
ITEMS = 'dagger'


solved_places = {'a1':False, 'a2':False, 'a3':False, 'a4':False,
                'b1':False, 'b2':False, 'b3':False, 'b4':False,
                'c1':False, 'c2':False, 'c3':False, 'c4':False,
                'd1':False, 'd2':False, 'd3':False, 'd4':False,
                }

zonemap = {
    'a1': {
        ZONENAME: "Town Market",
        DESCRIPTION: "This is your town's market. It's full of stalls which are full of gems, toys, and other things.",
        EXAMINATION: 'A man walks up to you asking if you want to taste some lettuce. You decline.',
        SOLVED: False,
        UP: '',
        DOWN: 'b1',
        LEFT: '',
        RIGHT: 'a2',
    },

    'a2': {
        ZONENAME: "Town Entrance",
        DESCRIPTION: "This is your town's Main Entrance.",
        EXAMINATION: 'The right side of the archway has some moss.',
        SOLVED: False,
        UP: '',
        DOWN: 'b2',
        LEFT: 'a1',
        RIGHT: 'a3',
    },

    'a3': {
        ZONENAME: "Town Square",
        DESCRIPTION: "This is your town's square.",
        EXAMINATION: 'Use your imagination!',
        SOLVED: False,
        UP: '',
        DOWN: 'b3',
        LEFT: 'a2',
        RIGHT: 'a4',
    },

    'a4': {
        ZONENAME: "Town Hall",
        DESCRIPTION: "This is your town's hall, where councillors meet up to discus new laws and destroy old ones.",
        EXAMINATION: 'Why are you examining this!',
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
        ITEMS: 'dagger',
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
        ITEMS: 'sword',
    },

    'c2': {
        ZONENAME: "Forest",
        DESCRIPTION: 'This area, lonely and full of trees, is part of a forest.',
        EXAMINATION: 'You notice some heather growing. You decide to take a rest on it for a while. \nYou find a sharp rock under you. You can pick it up',
        SOLVED: False,
        UP: 'b2',
        DOWN: 'd2',
        LEFT: 'c1',
        RIGHT: 'c3',
        ITEMS: 'rock',
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
        DESCRIPTION: 'This area, lonely and full of trees, is part of a forest.',
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
        UP: 'c3',
        DOWN: '',
        LEFT: 'd2',
        RIGHT: 'd4',
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


##### Game Interactivity #####
def print_location():
    print('\n' + ('#' * (4 + len(zonemap[my_player.location][DESCRIPTION]))))
    print('- ' + my_player.location.upper())
    print('- ' + zonemap[my_player.location][ZONENAME])
    print('- ' + zonemap[my_player.location][DESCRIPTION])
    print('#' * (4 + len(zonemap[my_player.location][DESCRIPTION])))

def prompt():
    print("\n" + "================================")
    print("What would you like to do?")
    action = input("> ")
    acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit', 'examine',
    'inspect', 'interact', 'look', 'exit', 'fight', 'run', 'attack', 'flee',
    'open', 'get', 'help']
    while action.lower() not in acceptable_actions:
        print('Unknown action, try again.\n')
        action = input("> ")
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        player_move()
    elif action.lower() in ['examine', 'inspect', 'look']:
        player_examine(action.lower())
    elif action.lower() in ['attack', 'fight']:
        player_fight()
    elif action.lower() in ['run', 'flee']:
        player_flee()
    elif action.lower() in ['open', 'get']:
        player_open()
    elif action.lower() == 'help':
        help_menu('game')

def player_move():
    ask = 'Where do you want to move?\n'
    dest = input(ask + '> ')
    while dest.lower() not in ['up', 'north', 'left', 'west', 'right', 'east', 'down', 'south']:
    	print('Command not understood. Try again.')
    	dest = input(ask + '> ')
    if dest.lower() in ['up', 'north']:
        on_edge(UP)
    elif dest.lower() in ['left', 'west']:
        on_edge(LEFT)
    elif dest.lower() in ['right', 'east']:
        on_edge(RIGHT)
    elif dest.lower() in ['down', 'south']:
        on_edge(DOWN)

def on_edge(direction):
    if zonemap[my_player.location][direction] == '':
        print('You bump into the edge of the world.')
        prompt()
    else:
        destination = zonemap[my_player.location][direction]
        movement_handler(destination)
        

def movement_handler(destination):
    print("\n" + "You have moved to the " + destination + ".")
    my_player.location = destination
    print_location()
    prompt()

def player_examine(action):
    if zonemap[my_player.location][SOLVED] == True:
        print("You have seen everything that there is to see here.")
    else:
        if action == 'examine':
            print(zonemap[my_player.location][EXAMINATION])
            prompt()

def player_fight():
    if zonemap[my_player.location][ZONENAME] == "Dungeon":
        if ['rock', 'dagger', 'sword'] in my_player.items:
            print("You defeated the monsters.")
        else:
            if my_player.hp >= 0:
                my_player.hp = my_player.hp - 10
                print('You have no weapons! You lose some health! Better run!')
                print('The value of your share in HP Sauce is: $' + str(my_player.hp) + '.')
                prompt()
            else:
                print('You died.')
                time.sleep(5)
                title_screen()
    else:
        print('You cannot do that here!')
        prompt()

def player_flee():
    print("You make a break for it!")
    player_move()

def player_open():
    if zonemap[my_player.location][ZONENAME] == 'Treasure Chest' or my_player.location == 'c2':
        my_player.items.append(zonemap[my_player.location][ITEMS])
        print('You found: ' + zonemap[my_player.location][ITEMS])
        prompt()
    else:
        print("You can't do that here!")
        prompt()

title_screen()