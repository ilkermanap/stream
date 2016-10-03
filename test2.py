from izleme.kayit import Kayit
from izleme.istemci import Istemci
import time

k = Kayit()
h = ("manap.se",20000)

s = Istemci(h,k)
while 1:
    
    s.gonder()
    time.sleep(5)
