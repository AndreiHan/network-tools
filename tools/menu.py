import os

from tools import network
from tools.ip import renew_ip
from tools.speed import speedtest_verbose
from tools.network import Network

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
        1: 'Network Status',
        2: 'Refresh Connection (Renew IP)',
        3: 'Speed Test',
        4: 'Exit',
    }
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


def clear():
    os.system('cls')


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
                network.display_all()
            elif option == 2:
                network.refresh_connection()
                network.display_all()

            elif option == 3:
                speedtest_verbose()

            elif option == 4:
                print('Bye now!')
                exit()
            else:
                print('Invalid option. Please enter a number between 1 and 4.')

            if 1 <= option <= 4:
                if ask_yesno("Do you want to go back? y/N") == 1:
                    clear()
                else:
                    print('Bye now!')
                    exit()
