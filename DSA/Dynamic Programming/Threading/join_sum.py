import threading
import time

class X(threading.Thread):
    def run(self):
        for i in range(101,201):
            if i == 151:
                time.sleep(3)
            print(i)
class Y(threading.Thread):
    def run(self):
        sum=0
        for j in range(1,101):
            sum+=j
        print(sum)
            
x1=X()
y1=Y()
x1.start()
x1.join(2)
y1.start()