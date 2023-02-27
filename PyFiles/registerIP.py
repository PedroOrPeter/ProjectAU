import socket


class GetIpByDevice:
    def __init__(self):
        self.hostname = None
        self.ip_address = None
        self.get_hostname()
        self.get_ip_address()

    def get_hostname(self):
        self.hostname = socket.gethostname()
        return self.hostname

    def get_ip_address(self):
        self.ip_address = socket.gethostbyname(self.hostname)
        return self.ip_address

# print(f"Hostname: {hostname}")
# print(f"IP Address: {ip_address}")
