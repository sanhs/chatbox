# TODO: create a server to accept connections and data
# TODO: send the data to received address

import sys
import socket
import _thread
import select

# CONN DETAILS
HOST = '127.0.0.1'
PORT = 8800
RECV_BUFFER = 4096
# Manage Connections
SOCKET_LIST = []
# SERVER MSGS
WELCOME_MESSAGE = 'Welcome to the server\n'.encode('utf-8')
# MSG TYPES
STRING_TYPE = 'utf-8'


def _handle_exception(msg, e):
    print(msg, e)
    sys.exit()


class Server:
    def __init__(self, port):
        super().__init__()

        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as e:
            _handle_exception('ERROR: creating socket', e)

        try:
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.bind((HOST, port))
        except socket.error as e:
            _handle_exception('ERROR: error binding socket', e)
        self.start_server(port)

    def start_server(self, port):
        self.socket.listen(10)
        print('Server started...\nlistening on port', port, '\nMaximum allowed connections 10')

    def create_server(self):
        return self.socket

    def manage_conn(self):
        SOCKET_LIST.append(self.socket)


class ClientThread:
    def __init__(self, client_conn, rec_conn):
        super().__init__()
        client_conn.send(WELCOME_MESSAGE)
        while 1:
            msg = client_conn.recv(1024)
            msg = self.decode_msg(self, msg, STRING_TYPE)
            print(msg)
            if not msg:
                break
                # rec_conn.sendall(msg.decode('utf-8'))
        client_conn.close()

    @staticmethod
    def decode_msg(self, msg, msg_type):
        return msg.decode(msg_type)


def main():
    server = Server(PORT).create_server()
    try:
        while 1:
            conn, addr = server.accept()
            print(addr, 'connected...')
            _thread.start_new_thread(ClientThread, (conn, conn,))
    except KeyboardInterrupt as e:
        _handle_exception('\nclosing chatBox', e)
        server.shutdown(socket.SHUT_RDWR)
        server.close()
        sys.exit()


if __name__ == '__main__':
    main()