import os
from tools.ip import renew_ip
from tools.network import network_status
from tools.speed import speedtest_verbose


def ask_yesno(question):
    """
    Helper to get yes / no answer from user.
    """
    yes = {'yes', 'y', 'Y', ''}

    no = {'no', 'n', 'N'}  # pylint: disable=invalid-name

    done = False
    print(question)
    while not done:
        choice = input().lower()
        if choice in yes:
            return True
        elif choice in no:
            return False
        else:
            print("Please respond by yes or no.")


def print_menu():
    menu_options = {
        1: 'Network Status',
        2: 'Refresh Connection (Renew IP)',
        3: 'Speed Test',
        4: 'Exit',
    }
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


def option1():
    network_status()


def option2():
    renew_ip()


def option3():
    print("Speed Test Is loading")
    print("")
    speedtest_verbose()
    print("")


def clear():
    os.system('cls')  # on Linux System


def main_menu():
    while True:
        print_menu()
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        # Check what choice was entered and act accordingly
        if option == 1:
            option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            print('Bye now!')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')
        if ask_yesno("Do you want to go back? y/N"):
            clear()
        else:
            print('Bye now!')
            exit()
