from tools.ip import get_gateway_ip, get_current_dns, get_local_ip, refresh_connection, renew_ip, flush_dns, \
    get_hostname
from tools.ping import ping_multiple
from tools.port import check_port_common_verbose


class Network:
    hostname = "localhost"
    local_ip = "0.0.0.0"
    dns = "0.0.0.0"
    gateway = "0.0.0.0"
    speed = None
    local_list = []
    common_dns = []
    current_config = {}

    def __init__(self):
        self.hostname = get_hostname()
        self.gateway = get_gateway_ip()
        self.dns = get_current_dns()
        self.local_ip = get_local_ip()

        self.local_list = ["localhost", "0:0:0:0:0:0:0:1", "127.0.0.1"]
        self.common_dns = ["1.1.1.1", "8.8.8.8", "1.0.0.1", "8.8.4.4"]
        self.local_list.append(self.local_ip)
        self.local_list.append(self.gateway)
        self.common_dns.append(self.dns)
        self.create_status_json()

    def status(self, speed_test):
        self.display_all()
        self.test_network()
        if speed_test:
            self.test_speed_verbose()
        self.check_ports_verbose()
        self.export()

    def export(self):
        import json
        self.create_status_json()
        json_object = json.dumps(self.current_config, indent=4)
        with open('output/status.json', 'w+') as openfile:
            openfile.write(json_object)
            openfile.close()

    def create_status_json(self):
        self.current_config["Hostname"] = self.hostname
        self.current_config["Local IP"] = self.local_ip
        self.current_config["Default Gateway"] = self.gateway
        self.current_config["Primary DNS"] = self.dns
        self.current_config["Speed"] = str(self.speed).replace("\r\n", " ")

    def check_ports_verbose(self):
        check_port_common_verbose(self.local_ip)

    def test_network(self):
        self.test_local_verbose()
        self.test_dns_verbose()

    def test_speed_verbose(self):
        if self.speed is not None:
            print(self.speed)
        else:
            print("Speed Test Running...")
            print("")
            self.test_speed()
            print(self.speed)

    def test_speed(self):
        from tools.speed import speedtest
        self.speed = speedtest().decode().strip()

    def test_local(self):
        return ping_multiple(self.local_list) == 1

    def test_local_verbose(self):
        if ping_multiple(self.local_list) == 1:
            print("Local Test Looks Good")

    def test_dns(self):
        return ping_multiple(self.common_dns) == 1

    def test_dns_verbose(self):
        if ping_multiple(self.common_dns) == 1:
            print("DNS Test Looks Good")

    def refresh_connection(self):
        refresh_connection()
        self.__init__()

    def renew_ip(self):
        renew_ip()
        self.__init__()

    def flush_dns(self):
        flush_dns()
        self.__init__()

    def display_all(self):
        self.display_hostname()
        self.display_local_ip()
        self.display_dns()
        self.display_gateway()
        self.display_speed()

    def display_hostname(self):
        print("Hostname: " + self.hostname)

    def display_speed(self):
        if self.speed is not None:
            print(self.speed)
        else:
            print("Speed is not yet measured")

    def display_local_ip(self):
        print("Local IP: " + self.local_ip)

    def display_dns(self):
        print("DNS: " + self.dns)

    def display_gateway(self):
        print("Default Gateway: " + self.gateway)
