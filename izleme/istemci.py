import socket
import time
from kayit import Kayit
import bz2

class Istemci:
    def __init__(self, sunucu, kayitci):
        self.merkez = sunucu  # must be in (host, port) format
        self.kayitci = kayitci
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def gonder(self):
        veri = self.kayitci.fark()
        print len(veri)
        self.socket.sendto(self.kayitci.fark(), self.merkez)

                        
