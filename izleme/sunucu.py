import socket
import bz2
import pickle
import cv2

class Sunucu:
    def __init__(self, port=20000):
        self.host= ""
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.host, self.port))
        self.clients = {}

    def receive(self, size=4096):
        data, addr = self.socket.recvfrom(size)
        f = pickle.loads(bz2.decompress(data))
        if addr in self.clients.keys():
            self.clients[addr][f[0]]= f[1]
            cv2.imwrite("%s%s.png" % (addr, f[0]))
