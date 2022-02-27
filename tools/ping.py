from tools.ip import get_current_dns, get_gateway_ip
import subprocess
import platform

def ping_gateway_verbose():
    if ping(get_gateway_ip()) == 1:
        print("Default Gateway can be reached")
    else:
        print("Default Gateway cannot be reached !!")


def ping_gateway():
    return ping(get_gateway_ip()) == 1


def ping_local_dns_verbose():
    if ping(get_current_dns()) == 1:
        print("Local DNS settings are valid")
    else:
        print("DNS server is unreachable")


def ping_local_dns():
    return ping(get_current_dns()) == 1


def check_list_availability(servers):
    res = ping_multiple_dictionary(servers)
    if len(list(set(list(res.values())))) == 1:
        if list(res.items())[0][1] == 1:
            return 1
    else:
        return 0


def check_list_availability_verbose(servers):
    res = ping_multiple_dictionary(servers)
    print("")
    print("####RESULT####")
    if len(list(set(list(res.values())))) == 1:
        if list(res.items())[0][1] == 1:
            print(servers)
            print("All servers are Online")
    else:
        print(res)
        print("Some servers are Offline")
    print("##############")
    print("")


def check_list_availability(servers):
    res = ping_multiple_dictionary(servers)
    if len(list(set(list(res.values())))) == 1:
        if list(res.items())[0][1] == 1:
            return 1
    else:
        return 0


def ping_multiple_dictionary(servers):
    servers_status = dict.fromkeys(servers, 0)
    for i in servers:
        if ping(i) == 1:
            servers_status[i] = 1

    return servers_status


def ping_multiple(servers):
    for i in servers:
        return ping(i) == 1


def ping_multiple_verbose(servers):
    """
    Prints every server with a status:
    localhost - Available
    1.1.1.1 - Offline
    """
    for i in servers:
        if ping(i) == 1:
            print(i, " -Available")
        else:
            print(i, " -Offline")


def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower() == 'windows' else '-c'


    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]
    return subprocess.call(command) == 0
