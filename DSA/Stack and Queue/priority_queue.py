class Priority_Queue:
    def __init__(self):
        self.queue = []
    
    def push(self,data):
        self.queue.append(data)
        
    def display(self):
        print(self.queue)
    
    def delete(self):
        self.queue.sort(reverse=True)
        print("Deleted Element:",self.queue.pop(0))
    
priority_quqeue_object = Priority_Queue()
priority_quqeue_object.push(7)
priority_quqeue_object.push(2)
priority_quqeue_object.push(1)
priority_quqeue_object.push(8)
priority_quqeue_object.push(5)
priority_quqeue_object.display()
priority_quqeue_object.delete()
priority_quqeue_object.display()