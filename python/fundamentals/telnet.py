import getpass
import telnetlib
import time
import re


def telnet_to_host(host, console_port, username, password):
    tn = telnetlib.Telnet(host,console_port)
    if username:
        tn.read_until(b"Username: ")
        tn.write(username.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
    tn.write(b"\n")
    tn.write(b"\n")
    return tn


def send_command_to_telnet(tn, command):
    tn.write(command.encode('ascii') + b'\n')
    time.sleep(7)


def read_telnet_session(tn):
    s = tn.read_very_eager().decode()
    return s


def close_telnet(tn):
    tn.close()
    
HOST = "x.x.x.x"
CONSOLE_PORT = 2047
USER = input("Enter your remote account: ")
PASSWORD = getpass.getpass("User Password: ")
tn = telnet_to_host(HOST, CONSOLE_PORT, None, None)

send_command_to_telnet(tn, "term len 0")
telnet_output = read_telnet_session(tn)
print(telnet_output)
