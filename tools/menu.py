import os
import platform
import subprocess
from tools.network import Network
from ssh.ssh_menu import ssh_main_menu

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
        1: 'Network Status - with Speed Test',
        2: 'Network Status - without Speed Test',
        3: 'Refresh Connection (Renew IP)',
        4: 'SSH Menu',
        5: 'Exit',
    }
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


def clear():
    import platform
    param = 'cls' if platform.system().lower() == 'windows' else 'clear'
    command = [param]
    return subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT) == 0


def main_menu():
    network = Network()

    while True:
        print_menu()

        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')

        else:
            if option == 1:
                network.status(True)
            elif option == 2:
                network.status(False)
            elif option == 3:
                network.refresh_connection()
                network.display_all()
            elif option == 4:
                clear()
                ssh_main_menu()
            elif option == 5:
                print('Bye now!')
                exit()
            else:
                print('Invalid option. Please enter a number between 1 and 4.')

            if 1 <= option <= 3:
                if ask_yesno("Do you want to go back? y/N") == 1:
                    clear()
                else:
                    print('Bye now!')
                    exit()
