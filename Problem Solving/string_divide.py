string = input()
parts = int(input())
if len(string) % parts != 0:
    print("Invalid String")
else:
    parts_list = []
    j=0
    for i in range(parts):
        parts_list.append(string[j:j+(len(string)//parts)])
        j+=(len(string)//parts)
    print(*parts_list)