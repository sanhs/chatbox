# client side of the chatbox

import sys
import socket

SERVER = '127.0.0.1'
PORT = 8800

def _handle_exception(msg, e):
    print(msg, e)
    sys.exit()


class Client:
    def __init__(self):
        super().__init__()
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as e:
            _handle_exception('ERROR: creating socket', e)
        try:
            remote_ip = socket.gethostbyaddr(SERVER)
        except socket.gaierror as e:
            _handle_exception('could not resolve host, or host is down', e)

        self.socket.connect((SERVER, PORT))
        try:
            self.socket.sendall('HI'.encode('utf-8'))
        except socket.error as e:
            _handle_exception('could not send request to server', e)

        while 1:
            self.socket.sendall(input('msg:').encode('utf-8'))
        while 1:
            reply = self.socket.recv(4096)
            reply = reply.decode('utf-8')
            print(reply)


def main():
    client_conn = Client()
    client_conn.close()


if __name__ == '__main__':
    main()