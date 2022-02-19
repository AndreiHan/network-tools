from tools.ip import get_gateway_ip, get_current_dns, get_local_ip, refresh_connection, renew_ip, flush_dns
from tools.ping import ping_multiple


class Network:
    local_ip = "0.0.0.0"
    dns = "0.0.0.0"
    gateway = "0.0.0.0"

    local_list = ["localhost", "0:0:0:0:0:0:0:1", "127.0.0.1"]
    common_dns = ["1.1.1.1", "8.8.8.8", "1.0.0.1", "8.8.4.4"]

    def __init__(self):
        self.gateway = get_gateway_ip()
        self.dns = get_current_dns()
        self.local_ip = get_local_ip()

        self.local_list.append(self.local_ip)
        self.local_list.append(self.gateway)
        self.common_dns.append(self.dns)

    def refresh_connection(self):
        refresh_connection()
        self.__init__()

    def renew_ip(self):
        renew_ip()
        self.__init__()

    def flush_dns(self):
        flush_dns()
        self.__init__()

    def local_test(self):
        return ping_multiple(self.local_list) == 1

    def local_test_verbose(self):
        if ping_multiple(self.local_list) == 1:
            print("Local Test Looks Good")

    def dns_test(self):
        return ping_multiple(self.common_dns) == 1

    def dns_test_verbose(self):
        if ping_multiple(self.common_dns) == 1:
            print("DNS Test Looks Good")

    def display_all(self):
        self.display_local_ip()
        self.display_dns()
        self.display_gateway()

    def display_local_ip(self):
        print("Local IP: " + self.local_ip)

    def display_dns(self):
        print("DNS: " + self.dns)

    def display_gateway(self):
        print("Default Gateway: " + self.gateway)
