def refresh_connection():
    flush_dns()
    renew_ip()


def renew_ip():
    import platform
    import subprocess
    if platform.system().lower() == 'windows':
        subprocess.call(["ipconfig", "/release"], shell=True)
        subprocess.call(["ipconfig", "/renew"], shell=True)
    else:
        subprocess.call(["sudo", "dhclient", "-r"], shell=True)
        subprocess.call(["sudo", "dhclient"], shell=True)


def flush_dns():
    import subprocess
    import platform
    if platform.system().lower() == 'windows':
        subprocess.call(["ipconfig", "/flushdns"], shell=True)
        subprocess.call(["netsh", "winsock", "reset", "catalog"], shell=True)
        subprocess.call(["netsh", "int", "ip", "reset"], shell=True)
    else:
        subprocess.call(["sudo", "systemd-resolve", "--flush-caches"], shell=True)
        subprocess.call(["sudo", "resolvectl", "flush-caches"], shell=True)


def get_current_dns():
    import dns.resolver
    dns_resolver = dns.resolver.Resolver()
    return dns_resolver.nameservers[0]


def get_gateway_ip_verbose():
    import netifaces
    gws = netifaces.gateways()
    gateway = gws['default'][netifaces.AF_INET][0]
    print("Gateway IP: " + gateway)


def get_gateway_ip():
    import netifaces
    gws = netifaces.gateways()
    gateway = gws['default'][netifaces.AF_INET][0]
    return gateway


def get_local_ip_verbose():
    import socket
    hostname = socket.gethostname()
    print("Local IP: " + socket.gethostbyname(hostname))


def get_local_ip():
    import socket
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)
