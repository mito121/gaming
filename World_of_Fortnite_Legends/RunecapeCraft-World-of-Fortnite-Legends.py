import random
import sys
import os

def clear_console():
    # Check the operating system to use the appropriate clear command
    if os.name == "posix":  # Unix-based systems (Linux, macOS)
        os.system("clear")
    elif os.name == "nt":   # Windows
        os.system("cls")


while True:
    print('''
         .
        ":"
      ___:____     |"\/"|
    ,'        `.    \  /
    |  O        \___/  |
~^~^~^~^~^~^~^~^~^~^~^~^~
    ''')
    # print(
    # '''
    #     __________________
    #     |@@@@@|     |####|
    #     |@@@@@|     |####|
    #     |@@@@@|     |####|
    #      \@@@@|     |####/
    #       \@@@|     |###/
    #        `@@|_____|##'
    #             (O)
    #         .-\'\'\'''-.
    #       .'  * * *  `.
    #      :  *       *  :
    #     : ~    NERD   ~ :
    #     : ~ A W A R D ~ :
    #      :  *       *  :
    #       `.  * * *  .'
    #         `-.....-'
    # ''' 
    # )
    print("\nWelcome to the greatest game ever.\nRoll the dice start the game.\n\n")
    print(''' 1. Roll the dice             2. exit     ''')

    userInput = int(input("What would you like to do?\n"))
    rolls = []
    min = 1
    max = 100
    hasLost = False

    if userInput == 1:
        while hasLost == False:
            roll = random.randint(min, max)

            if roll == 1:
                print(
            '''
                __________________
                |@@@@@|     |####|
                |@@@@@|     |####|
                |@@@@@|     |####|
                 \@@@@|     |####/
                  \@@@|     |###/
                   `@@|_____|##'
                        (O)
                    .-\'\'\'''-.
                  .'  * * *  `.
                 :  *       *  :
                : ~    NERD   ~ :
                : ~ A W A R D ~ :
                 :  *       *  :
                  `.  * * *  .'
                    `-.....-'
            ''' 
                )
                print("CONGRATULATIONS! YOU ROLLED 1 AND WON THE GAME!!!")
                continuePlaying = int(input(''' 1. Win again             2. Quit while still on top     \n'''))

                if continuePlaying == 1:
                    break
                else:
                    clear_console()
                    sys.exit()

            if len(rolls) == 0:
                rolls.append(roll)
                print("\n-------------------------------------------------------\n")
                print(f'You rolled {roll}. Roll lower to keep playing.\n')

                continuePlaying = int(input(''' 1. Roll the dice             2. exit     \n'''))

                if continuePlaying == 1:
                    continue
                else:
                    clear_console()
                    sys.exit()

            else:
                if roll > rolls[-1]:  # Compare with the last roll
                    print(
                        '''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀██    ██  ██████  ██    ██     ███████ ██    ██  ██████ ██   ██ 
                 ██  ██  ██    ██ ██    ██     ██      ██    ██ ██      ██  ██  
                  ████   ██    ██ ██    ██     ███████ ██    ██ ██      █████   
                   ██    ██    ██ ██    ██          ██ ██    ██ ██      ██  ██  
                   ██     ██████   ██████      ███████  ██████   ██████ ██   ██
                        '''
                        )
                    continuePlaying = int(input((f"You rolled {roll} which is HIGHER than {rolls[-1]}, which means you lost. Press 1 to test your IQ again.\n")))
                    if continuePlaying == 1:
                        clear_console()
                        break
                    else:
                        clear_console()
                        sys.exit()

                rolls.append(roll)
                print("\n-------------------------------------------------------\n")
                print(f'You rolled {roll} which is lower than {rolls[-2]}. Roll lower again to keep playing.\n')

                continuePlaying = int(input(''' 1. Roll the dice             2. exit     \n'''))

                if continuePlaying == 1:
                    continue
                else:
                    clear_console()
                    sys.exit()
    else:
        break