from kamera import Kamera
import cv2
import time
import pickle

class Kayit:
    def __init__(self,kamera1 = None):
        if kamera1 is None:
            self.kamera = Kamera()
        else:
            self.kamera = kamera1
        self.kamera.kamera.set(3,320)
        self.kamera.kamera.set(4,200)
        self.onceki = self.kamera.resim()
        self.guncel = None
    
    def fark(self, num = 0, thres = 100):
        print "fark"
        self.guncel = self.kamera.resim()
        ret, gri_guncel = cv2.threshold(cv2.cvtColor(self.guncel, cv2.COLOR_BGR2GRAY), thres, 255, cv2.THRESH_BINARY)
        ret, gri_onceki = cv2.threshold(cv2.cvtColor(self.onceki, cv2.COLOR_BGR2GRAY), thres, 255, cv2.THRESH_BINARY) 
    
        degisim = gri_onceki - gri_guncel
        cv2.imwrite("degisim%03d.png" % num, degisim)
        self.onceki = self.guncel
        ts = time.strftime("%Y%m%d-%H%M%S")        
        return bz2.compress(pickle.dumps([ts,self.guncel]))
