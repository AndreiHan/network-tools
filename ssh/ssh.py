import paramiko



def send_script(hostname, username, password):
    # initialize the SSH client
    client = paramiko.SSHClient()
    # add to known hosts
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=hostname, username=username, password=password)
    except:
        print("[!] Cannot connect to the SSH Server")
        exit()

    # execute the commands

    # read the BASH script content from the file
    bash_script = open("../input/script.sh").read()

    # execute the BASH script
    stdin, stdout, stderr = client.exec_command(bash_script)
    # read the standard output and print it
    print(stdout.read().decode())

    # print errors if there are any
    err = stderr.read().decode()
    if err:
        print(err)

    # close the connection
    client.close()


def send_commands(commands, hostname, username, password):
    # initialize the SSH client
    client = paramiko.SSHClient()
    # add to known hosts
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=hostname, username=username, password=password)
    except:
        print("[!] Cannot connect to the SSH Server")
        exit()

    for command in commands:
        print("=" * 50, command, "=" * 50)
        stdin, stdout, stderr = client.exec_command(command)
        print(stdout.read().decode())
        err = stderr.read().decode()
        if err:
            print(err)
        client.close()
