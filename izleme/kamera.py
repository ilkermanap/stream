import cv2


class Kamera:
    def __init__(self, port = 0):
        self.port = port
        self.kamera = cv2.VideoCapture(self.port)

    def resim(self):
        kod, resim = self.kamera.read()
        return resim

    def kaydet(self, dosya_adi):
        cv2.imwrite(dosya_adi, self.resim())
        
        
