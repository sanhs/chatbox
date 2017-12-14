
import sys
import socket
import _thread
import threading
import select


HOST = '127.0.0.1'
PORT = 8800
RECEIVE_BUFFER = 4096
WELCOME_MSG = 'Welcome to the server...\n'
STRING_TYPE = 'utf-8'
CLIENT_CLOSE_SIGNAL = int('0xff', 16)
CLIENTS = {}


class Server:
    def __init__(self):
        super().__init__()
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.bind((HOST, PORT))
            self.socket.listen(10)
        except socket.error as e:
            print('error creating socket', e)
            sys.exit()

    def create_server(self):
        return self.socket


class Client:
    def __init__(self, conn, addr, nick):
        super().__init__()
        self.conn = conn
        self.ip = addr[0]
        self.port = addr[1]
        self.conn.sendall(WELCOME_MSG.encode(STRING_TYPE))
        _thread.start_new_thread(self.read_client_msg, ())
        self.send_client_msg()
        print(nick, 'threads created...')

    def read_client_msg(self):
        try:
            while 1:
                read_in, write_in, error_in = select.select([self.conn], [], [self.conn], 0)
                if read_in:
                    msg = self.conn.recv(RECEIVE_BUFFER)
                    if msg:
                        msg = msg.rstrip()
                        print(str(self.ip)+':'+str(self.port), ':', msg.decode(STRING_TYPE))
                    else:
                        break
        finally:
            self.close_conn()

    def send_client_msg(self):
        while 1:
            reply = input('')
            reply = reply + '\n'
            self.conn.sendall(reply.encode(STRING_TYPE))

    def close_conn(self):
        print(self.ip, 'disconnected...\nclosing connection')
        self.conn.close()


def send_client_msg(conn, msg):


def read_client_msg(conn, nick, r_nick):
    r_conn, r_addr, r_nick = CLIENTS[r_nick]
    try:
        while 1:
            read_in, write_in, error_in = select.select([conn], [], [conn], 0)
            if read_in:
                msg = conn.recv(RECEIVE_BUFFER)
                if msg:
                    send_client_msg(r_conn, msg)
    finally:
        print(nick, 'disconnected\n closing connection')


def accept_conn(server):
    print('listening on 8800...')
    conn, addr = server.accept()
    print(addr[0], ':', addr[1], 'connected')
    conn.sendall('NICK:'.encode(STRING_TYPE))
    nick = conn.recv(RECEIVE_BUFFER)
    while not nick:
        nick = conn.recv(RECEIVE_BUFFER)
    nick = nick.rstrip()
    CLIENTS[nick] = (conn, addr, nick, )
    Client(conn, addr, nick)


def main():
    server = Server().create_server()
    try:
        while 1:
            accept_conn(server)
    except KeyboardInterrupt:
        print('Keyboard Interrupt\nclosing connection\nexiting...')
        server.close()
        sys.exit()


if __name__ == '__main__':
    main()
