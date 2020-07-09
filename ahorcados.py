# Juego del ahorcado
# by @M4lal0
# -*- coding: utf-8 -*-

import random,os,time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

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

WORDS_EASY = ('pelicula','obligacion','estados','fuego','cara','sofa','gobierno','camisa','adulto','aire','mesa','pan','volcan')
WORDS_MEDIUM= ('microsoft','facebook','tesla','twitter','amazon','telefonica','avioneta','democracia','computadora','gobierno')
WORDS_HARD = ('anticonstitucionalmente','parangaricutirimicuaro','otorrinolaringologia','institucionalizacion','esternocleidomastoideo','electroencefalograma')


def random_word(option):
    if option == "1":
        idx = random.randint(0, len(WORDS_EASY) - 1)
        return WORDS_EASY[idx]
    elif option == "2":
        idx = random.randint(0, len(WORDS_MEDIUM) - 1)
        return WORDS_MEDIUM[idx]
    elif option == "3":
        idx = random.randint(0, len(WORDS_HARD) - 1)
        return WORDS_HARD[idx]
    else:
        return None


def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('--- * --- * --- * --- * --- * --- ')


def display_banner():
    banner = "\n ╔═══╗╔╗                    ╔╗    \n"
    banner += " ║╔═╗║║║                    ║║    \n"
    banner += " ║║ ║║║╚═╗╔══╗╔═╗╔══╗╔══╗ ╔═╝║╔══╗\n"
    banner += " ║╚═╝║║╔╗║║╔╗║║╔╝║╔═╝╚ ╗║ ║╔╗║║╔╗║\n"
    banner += " ║╔═╗║║║║║║╚╝║║║ ║╚═╗║╚╝╚╗║╚╝║║╚╝║\n"
    banner += " ╚╝ ╚╝╚╝╚╝╚══╝╚╝ ╚══╝╚═══╝╚══╝╚══╝\n"
    banner += "--[ Juego del ahorcado | v20.02 ]--"
    return print(bcolors.OKBLUE + banner + bcolors.ENDC)


def main():
    display_banner()
    print("\nOptions:")
    print("[1] - Easy")
    print("[2] - Medium")
    print("[3] - Hard")
    option = input("Select an option [1-3]: ")
    if option == "1" or option == "2" or option == "3":
        os.system('cls')
        word = random_word(option)
        hidden_word = ['-'] * len(word)
        tries = 0

        while True:
            os.system('cls')
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
                    os.system('cls')
                    display_banner()
                    display_board(hidden_word, tries)
                    print(bcolors.FAIL + "\n¡Game over! You lost. The correct word was: {0}".format(word) + bcolors.ENDC)
                    break
            else:
                for idx in letter_indexes:
                    hidden_word[idx] = current_letter

                letter_indexes = []

            try:
                hidden_word.index('-')
            except ValueError:
                os.system('cls')
                display_banner()
                display_board(hidden_word, tries)
                print(bcolors.OKGREEN + "\n¡Congratulation! You win. The word is: {0}".format(word) + bcolors.ENDC)
                break
    else:
        print("Option invalid!")
        time.sleep(1)
        os.system('ctrl + c')
        os.system('cls')


if __name__ == '__main__':
    main()