class Reverse_String:
    def __init__(self):
        self.string = []
        self.r_string = []
    
    def get_string(self,data):
        for i in data:
            self.string.append(i)
    
    def pop_str(self):
        print("Deleted Char:",self.string.pop())
    
    def display(self):
        my_string = ''
        for i in self.string:
            my_string += i
        print(my_string)
        
    def reverse_str(self):
        while self.string:
            self.r_string += self.string.pop()
        r_str = ''
        for i in self.r_string:
            r_str += i
        print(r_str)

string = input()
rev_str = Reverse_String()
rev_str.get_string(string)
rev_str.display()
rev_str.reverse_str()