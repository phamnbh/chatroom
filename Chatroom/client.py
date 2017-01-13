import socket

class Client:
    def __init__(self, host, port):
        self.socket = socket.socket()
        self.port = port
        self.host = host

    def run(self):
        self.socket.connect((self.host, self.port))
        print (self.sock.get.recv(1024).decode())
        


