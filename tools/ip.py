import dns.resolver
import netifaces


def refresh_connection():
    flush_dns()
    renew_ip()


def renew_ip():
    import platform
    import subprocess
    if platform.system().lower() == 'windows':
        subprocess.call(["ipconfig", "/release"], shell=True,stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)
        subprocess.call(["ipconfig", "/renew"], shell=True,stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)
    else:
        subprocess.call(["sudo", "dhclient", "-r"], shell=True,stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)
        subprocess.call(["sudo", "dhclient"], shell=True,stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)


def flush_dns():
    import subprocess
    import platform
    if platform.system().lower() == 'windows':
        subprocess.call(["ipconfig", "/flushdns"], shell=True,stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)
        subprocess.call(["netsh", "winsock", "reset", "catalog"], shell=True,stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)
        subprocess.call(["netsh", "int", "ip", "reset"], shell=True,stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)
    else:
        subprocess.call(["sudo", "systemd-resolve", "--flush-caches"], shell=True,stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)
        subprocess.call(["sudo", "resolvectl", "flush-caches"], shell=True,stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)


def get_hostname():
    import socket
    return socket.gethostname()


def get_current_dns():
    dns_resolver = dns.resolver.Resolver()
    return dns_resolver.nameservers[0]


def get_gateway_ip_verbose():
    gws = netifaces.gateways()
    gateway = gws['default'][netifaces.AF_INET][0]
    print("Gateway IP: " + gateway)


def get_gateway_ip():
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
