from ssh.fileManager import checkFile


def check():
    error_counter = 0
    if not ping_ip():
        error_counter += 1

    if error_counter > 0:
        print("Number of checks failed: " + str(error_counter))
    else:
        print("All check passed")


def ping_ip():
    from tools.ping import ping
    if checkFile():
        with open('input/ssh-credentials.txt') as f:
            return ping(f.readline().rstrip())
