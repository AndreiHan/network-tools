import socket
from contextlib import closing


def check_port_common_verbose(host):
    print("For Local IP: ")
    if check_port(host, 22) == 1:
        print("Port 22 is open")
    else:
        print("Port 22 is closed")

    if check_port(host, 80) == 1:
        print("Port 80 is open")
    else:
        print("Port 80 is closed")

    if check_port(host, 443) == 1:
        print("Port 443 is open")
    else:
        print("Port 443 is closed")


def check_port(host, port):
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        return sock.connect_ex((host, port)) == 0


def check_port_verbose(host, port):
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        if sock.connect_ex((host, port)) == 0:
            print("Port is open")
        else:
            print("Port is not open")
