from connect4 import connect4


if __name__ == '__main__':
    print("Welcome to Command Line Games!")
    print("So far we only have one game, so enjoy playing connect 4:")
    while 1:
        connect4()
        again = input("Would you like to play again? [y/n] ").lower()
        if  again == 'n' or again == "no":
            break
    print("Thank you for playing")