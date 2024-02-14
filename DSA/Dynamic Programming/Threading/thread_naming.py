import threading

class X(threading.Thread):
    def run(self):
        print(self.getName())

class Y(threading.Thread):
    def run(self):
        print(self.getName())
        
x1 = X()
x1.setName("X-Thread")
x1.start()
y1 = Y()
y1.setName("Y-Thread")
y1.start()