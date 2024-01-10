# def d(*a):
#     print(a)
#     print(type(a))
#     print(sum(a))
# d(10,20,30)
# d(1,2,3,4,5)

# # o/p:
# # (10, 20, 30)
# # <class 'tuple'>
# # 60
# # (1, 2, 3, 4, 5)
# # <class 'tuple'>
# # 15

# def d(b,*a):
#     print(a)
#     print(b)
#     print(sum(a)+b)
# d(10,20,30)

# o/p:
# (20, 30)
# 10
# 60


class test:
    def op(self,d,*a):
        if(d=="int"):
            s1 = 0
        else:
            s1 = ''
        for i in a:
            s1 = s1 + i 
        print(s1)
t1 = test()
t1.op("int",10,20,30)
t1.op("str","krishna","rama","Hanuman")

# o/p:
# 60
# krishnaramaHanuman