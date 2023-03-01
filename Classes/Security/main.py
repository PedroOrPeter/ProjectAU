from registerIP import *
from CmdControl import *


root = GetIpByDevice()


def capture_ip_device():
    root.get_hostname()
    if root:
        root.get_ip_address()


def wrt_read_txt():
    try:
        root.open_txt()
        root.write_txt()
        root.close_txt()
    except PermissionError:
        print(err)


def hide_file():
    root.hide_files()


if __name__ == '__main__':
    capture_ip_device()
    if wrt_read_txt():
        hide_file()
    try:
        start_server()
    except PermissionError as err:
        print(err)
