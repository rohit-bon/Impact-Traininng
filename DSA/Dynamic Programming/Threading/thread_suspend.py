import threading
import time

class X(threading.Thread):
    def run(self):
        time.sleep(10)
        for i in range(1,11):
            print("Rohit Thread:")

class Y(threading.Thread):
    def run(self):
        for j in range(1,6):
            print("Bongade Thread:")
            time.sleep(3)

x1=X()
x1.start()
y1=Y()
y1.start()