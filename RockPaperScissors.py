import random


def play():
    # Force user to prompt the correct variables
    flag = True
    print("\nHOW TO PLAY:")
    print("'r' for rock, 'p' for paper, 's' for scissors")
    while flag:
        user = input("\nEnter your choice:")
        user = user.strip()
        user = user.lower()
        if (user == "r") or (user == "p") or (user == "s"):
            flag = False
        else:
            print("Please input either 'r' , 'p' , or 's'")

    computer = random.choice(['r', 'p', 's'])

    # If user and computer is the same, nobody wins
    if user == computer:
        print("It's a tie!")
        print("The computer chose", computer)
        return 0

    if is_win(user, computer):
        print("You Won!")
        print("The computer chose", computer)
        return 0

    print("You Lost!")
    print("The computer chose", computer)
    return 0


def is_win(user, computer):
    """
    Determine whether user beats computer
    :param user: Input from user
    :param computer: Random choice from computer
    :return: True if user wins
    """
    if (user == "r" and computer == "s") or (user == "s" and computer == "p") or (user == "p" and computer == "r"):
        return True

