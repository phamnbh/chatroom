import socket
import urllib.request
import urllib
import re

class Server:
    def __init__(self, port):
        self.socket = socket.socket()
        self.host = getIP()
        self.port = port
        self.c = None
        self.addr = None

    def getIP(self):
        data = re.search('"([0-9.]*)"', urllib.request.urlopen("http://ip.jsontest.com/").read().decode()).group(1)
        return data

    def run(self):
        print("Server Info: " , self.getIP() , ", " , self.port)
        self.socket.bind((self.host, self.port))
        self.socket.listen()
        
        while True:
            self.c, self.addr = self.socket.accept()
            print("Connected to ", self.addr)
            self.c.send("Test".encode())
            self.c.close()
