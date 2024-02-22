#DFS - write a program to implement the DFS to python programming
# without recurssion

stack=[]
visited=[]
graph = {'5':['3','9'], '3':['2','4'], '9':['7','10'], '4':[], '2':[], '7':[], '10':[]}
def DFS(node,visited,graph):
    stack.append(node)
    visited.append(node)
    while(stack):
        m=stack.pop()
        print(m,end="")
        for p in graph[m]:
            if p not in visited:
                stack.append(p)
                visited.append(p)
print("DFS operation : ")
DFS('5',visited,graph)

# With recurssion

# visited=[]
# graph = {'5':['3','9'], '3':['2','4'], '9':['7','10'], '4':[], '2':[], '7':[], '10':[]}
# def DFS(node,visited):
#     if node not in visited:
#         visited.append(node)
#         print(node,end=" ")

#     for p in graph(node):
#         DFS(p,visited)

# print("DFS operation : ")
# DFS('5',visited,graph)