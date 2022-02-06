from tools.ip import get_local_ip_verbose, get_gateway_ip_verbose
from tools.ping import check_list_availability_verbose, ping_local_dns_verbose, ping_gateway_verbose, ping_gateway, \
    ping_local_dns, check_list_availability


def network_status():
    get_local_ip_verbose()
    get_gateway_ip_verbose()
    ping_gateway_verbose()
    ping_local_dns_verbose()
    servers_dns = ["8.8.8.8", "1.1.1.1", "localhost"]
    servers_local = ["localhost", "0:0:0:0:0:0:0:1", "127.0.0.1"]
    check_list_availability_verbose(servers_dns)
    check_list_availability_verbose(servers_local)
    if ping_gateway() == ping_local_dns() == check_list_availability(servers_dns) ==\
            check_list_availability(servers_local):
        print("All IS UP AND RUNNING")
    else:
        print("There Might Be Some Issues")


