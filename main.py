from ssh.ssh_menu import ssh_main_menu
from tools.menu import main_menu

def find_menu(x):
    if(x == 1):
        main_menu()
    elif x == 2:
        ssh_main_menu()

if __name__ == "__main__":
    main_menu()
