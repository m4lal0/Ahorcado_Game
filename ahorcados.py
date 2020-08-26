#!/usr/bin/python3
# Juego del ahorcado
# by @M4lal0
# -*- coding: utf-8 -*-

import random
import subprocess,sys
import platform
import time
import base64

class bcolors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    DARKCYAN = '\033[36m'
    UNDERLINE = '\033[4m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'


IMAGES = ['''
    +---+
    |   |
        |
        |
        |
        |
        =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''
    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''
    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''
    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

WORDS_EASY = ('cGVsaWN1bGE=','b2JsaWdhY2lvbg==','ZXN0YWRvcw==','ZnVlZ28=','Y2FyYQ==','c29mYQ==','Y2FtaXNh','YWR1bHRv','YWlyZQ==','bWVzYQ==','cGFu','dm9sY2Fu')
WORDS_MEDIUM = ('bWljcm9zb2Z0','ZmFjZWJvb2s=','dGVzbGE=','dHdpdHRlcg==','YW1hem9u','dGVsZWZvbmljYQ==','YXZpb25ldGE=','ZGVtb2NyYWNpYQ==','Y29tcHV0YWRvcmE=','Z29iaWVybm8=')
WORDS_HARD = ('YW50aWNvbnN0aXR1Y2lvbmFsbWVudGU=','cGFyYW5nYXJpY3V0aXJpbWljdWFybw==','b3RvcnJpbm9sYXJpbmdvbG9naWE=','aW5zdGl0dWNpb25hbGl6YWNpb24=','ZXN0ZXJub2NsZWlkb21hc3RvaWRlbw==','ZWxlY3Ryb2VuY2VmYWxvZ3JhbWE=')


def random_word(option):
    if option == "1":
        idx = random.randint(0, len(WORDS_EASY) - 1)
        return decodeBase64(WORDS_EASY[idx])
    elif option == "2":
        idx = random.randint(0, len(WORDS_MEDIUM) - 1)
        return decodeBase64(WORDS_MEDIUM[idx])
    elif option == "3":
        idx = random.randint(0, len(WORDS_HARD) - 1)
        return decodeBase64(WORDS_HARD[idx])
    else:
        return None


def decodeBase64(theword):
    base64_message = theword
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    return message


def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('--- * --- * --- * --- * --- * --- ')


def Clear():
    subprocess.Popen( "cls" if platform.system() == "Windows" else "clear", shell=True)
    time.sleep(0.1)


def display_banner():
    banner = "\n ╔═══╗╔╗                    ╔╗    \n"
    banner += " ║╔═╗║║║                    ║║    \n"
    banner += " ║║ ║║║╚═╗╔══╗╔═╗╔══╗╔══╗ ╔═╝║╔══╗\n"
    banner += " ║╚═╝║║╔╗║║╔╗║║╔╝║╔═╝╚ ╗║ ║╔╗║║╔╗║\n"
    banner += " ║╔═╗║║║║║║╚╝║║║ ║╚═╗║╚╝╚╗║╚╝║║╚╝║\n"
    banner += " ╚╝ ╚╝╚╝╚╝╚══╝╚╝ ╚══╝╚═══╝╚══╝╚══╝\n"
    banner += "--[ Juego del ahorcado | v20.02 ]--"
    return print(bcolors.DARKCYAN + banner + bcolors.ENDC)


def main():
    display_banner()
    print("""\nDifficulty:
    [1] - Easy
    [2] - Medium
    [3] - Hard""")
    option = input("Select an option [1-3]: ")
    if option == "1" or option == "2" or option == "3":
        Clear()
        word = random_word(option)
        hidden_word = ['-'] * len(word)
        tries = 0

        while True:
            Clear()
            display_banner()
            display_board(hidden_word, tries)
            current_letter = str(input('Type a letter: '))

            letter_indexes = []
            for idx in range(len(word)):
                if word[idx] == current_letter:
                    letter_indexes.append(idx)

            if len(letter_indexes) == 0:
                tries += 1

                if tries == 7:
                    Clear()
                    display_banner()
                    display_board(hidden_word, tries)
                    print(bcolors.RED + "\n¡Game over! You lost. The correct word was: {0}".format(word) + bcolors.ENDC)
                    break
            else:
                for idx in letter_indexes:
                    hidden_word[idx] = current_letter

                letter_indexes = []

            try:
                hidden_word.index('-')
            except ValueError:
                Clear()
                display_banner()
                display_board(hidden_word, tries)
                print(bcolors.GREEN + "\n¡Congratulation! You win. The word is: {0}".format(word) + bcolors.ENDC)
                break
    else:
        print("Option invalid!")
        time.sleep(1)
        sys.exit(1)


if __name__ == '__main__':
    main()