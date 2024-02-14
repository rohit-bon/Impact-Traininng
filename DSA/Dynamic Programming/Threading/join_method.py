import threading
import time


class Y(threading.Thread):
    def run(self):
        for i in range(1,6):
            print("Rohit Thread:")
            time.sleep(2)
y1=Y()
y1.start()
y1.join(5)
for j in range(1,11):
    print("Bongade Thread:")