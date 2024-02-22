#write a program to implement the BFS to python programming

queue = []
visited = []
graph = {'5':['3','9'], '3':['2','4'], '9':['7','10'], '2':[], '3':[], '7':[], '10':[]}
def BFS(node,visited,graph):
    queue.append(node)
    visited.append(node)
    while(queue):
        m=queue.pop(0)
        print(m,end=" ")
        for p in graph[m]:
            if p not in visited:
                queue.append(p)
                visited.append(p)
print("BFS operation : ")
BFS('5',visited,graph)
