import socket
import os


class GetIpByDevice:
    def __init__(self):
        self.hostname = None
        self.ip_address = None
        self.file = None

    def get_hostname(self):
        self.hostname = socket.gethostname()
        return self.hostname

    def get_ip_address(self):
        self.ip_address = socket.gethostbyname(self.hostname)
        return self.ip_address

    def open_txt(self):
        self.file = open('IpContent.txt', 'w')
        return self.file

    def write_txt(self):
        self.file.write('{}\n{}'.format(self.hostname, self.ip_address))

    def close_txt(self):
        self.file.close()

    def hide_files(self):
        os.system('attrib +h IpContent.txt')


GetIpByDevice()
