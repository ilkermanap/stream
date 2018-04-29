import cv2
import time

class Kamera:
    def __init__(self, port = 0):
        self.port = port
        self.kamera = cv2.VideoCapture(self.port)

    def resim(self):
        kod, resim = self.kamera.read()
        return resim

    def kaydet(self, dosya_adi):
        cv2.imwrite(dosya_adi, self.resim())
        
        
class TimeLapse(Kamera):
    def __init__(self, port=0):
        Kamera.__init__(self, port=port)
        

    def start(self, sleep_duration, num_pictures, prefix):
        for i in range(num_pictures):
            fname = "%s_%04d.png" % (prefix, i)
            self.kaydet(fname)
            print "frame ",i
            time.sleep(sleep_duration)
    
