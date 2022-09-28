from RockPaperScissors import *
from HangMan import *


def get_input():
    print("CHOOSE YOUR GAME!")
    print("(1) HangMan")
    print("(2) Rock Paper Scissors")
    print("(0) To Exit the game!")
    choice = int(input())

    return choice


if __name__ == '__main__':
    print()
    print("========WELCOME TO THE GAME PLATFORM========")
    print("+++++++ALL GAMES ARE WRITTEN IN PYTHON++++++")
    print("===========LET\'S GET STARTED!==============")

    choice = get_input()
    while choice != 0:
        if choice == 1:
            hangman()
            choice = get_input()
        elif choice == 2:
            play()
            choice = get_input()
        else:
            print("Your choice is not identified. Please try again")

    print("========THANK YOU FOR PLAYING========")


