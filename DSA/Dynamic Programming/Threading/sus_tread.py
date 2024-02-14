import threading
import time


class X(threading.Thread):
    def run(self):
        time.sleep(2)
        for i in range(1,101):
            print(i)

class Y(threading.Thread):
    def run(self):
        for j in range(101,201):
            print(j)
            
x1=X()
x1.start()
y1=Y()
y1.start()