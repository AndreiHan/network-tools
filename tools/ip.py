def renew_ip():
    import subprocess
    subprocess.call(["ipconfig", "/flushdns"], shell=True)
    subprocess.call(["ipconfig", "/release"], shell=True)
    subprocess.call(["ipconfig", "/renew"], shell=True)
    get_local_ip_verbose()


def get_current_dns():
    import dns.resolver
    import netifaces
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
