import os
from ssh.ssh import send_script, send_commands


def ask_yesno(question):
    """
    Helper to get yes / no answer from user.
    """
    yes = {'yes', 'y', 'Y', ''}

    no = {'no', 'n', 'N'}

    done = False
    print(question)
    while not done:
        choice = input().lower()
        if choice in yes:
            return True
        elif choice in no:
            return False
        else:
            print("Please respond by yes(y/Y) or no(n/Y)")


def print_menu():
    menu_options = {
        1: 'SSH Checks',
        2: 'Send Script File',
        3: 'Send Custom Command',
        4: 'Back'
    }
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


def clear():
    os.system('cls')


def ssh_main_menu():
    while True:
        print_menu()

        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')

        else:
            if option == 1:
                from ssh.check import check
                check()
            elif option == 2:
                send_script()
            elif option == 3:
                send_commands()
            elif option == 4:
                clear()
                break
            else:
                print('Invalid option. Please enter a number between 1 and 4.')

            if 1 <= option <= 3:
                if ask_yesno("Do you want to go back? y/N") == 1:
                    clear()
                else:
                    print('Bye now!')
                    exit()
