a,b,c = map(int, input().split(" "))
print("equal" if(a==b==c) else "a is max" if(a>b and a>c) else "b is max" if(b>c) else "c is max")
