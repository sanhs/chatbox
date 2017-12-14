
import sys
import socket
import select
import _thread

HOST = '127.0.0.1'
PORT = 8800
RECEIVE_BUFFER = 4096
STRING_TYPE = 'utf-8'


class Client:
    def __init__(self):
        super().__init__()

        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((HOST, PORT))
        except socket.error or socket.gaierror as e:
            print('could not connect to server...', e)
            sys.exit()

    def server_connection(self):
        return self.socket


def read_msg(conn):
    while 1:
        read_in, write_in, error_in = select.select([conn], [], [conn], 0)
        if read_in:
            msg = conn.recv(RECEIVE_BUFFER)
            if msg:
                msg = msg.rstrip()
                print(msg.decode(STRING_TYPE))
            else:
                break


def main():
    conn = Client().server_connection()
    try:
        _thread.start_new_thread(read_msg, (conn, ))
        while 1:
            reply = input('')
            reply = reply + '\n'
            conn.sendall(reply.encode(STRING_TYPE))
    except KeyboardInterrupt:
        print('Keyboard Interrupt\nclosing connection\nexiting...')
        _thread.exit()
        conn.close()
        sys.exit()


if __name__ == '__main__':
    main()