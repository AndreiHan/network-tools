from tools.ip import *
from tools.ping import ping, ping_multiple


class Network:
    local_ip = "0.0.0.0"
    dns = "0.0.0.0"
    gateway = "0.0.0.0"

    local_list = ["localhost", "0:0:0:0:0:0:0:1", "127.0.0.1"]

    def __init__(self):
        self.gateway = get_gateway_ip()
        self.dns = get_current_dns()
        self.local_ip = get_local_ip()

        self.local_list.append(self.local_ip)
        self.local_list.append(self.gateway)

    def self_test(self):
        if ping_multiple(self.local_list) == 1:
            print("All looks good")

    def display_local_ip(self):
        print("Local IP: " + self.local_ip)

    def display_dns(self):
        print("DNS: " + self.dns)

    def display_gateway(self):
        print("Default Gateway: " + self.gateway)

    def display_all(self):
        self.display_local_ip()
        self.display_dns()
        self.display_gateway()
