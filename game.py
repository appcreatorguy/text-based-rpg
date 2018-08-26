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
