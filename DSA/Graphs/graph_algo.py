def min_distance(V, dist, visisted):
    min = 9999
    for i in range(V):
        if dist[i] < min and visisted[i] == False:
            min = dist[i]
            min_index = i
    return min_index
def dijkstra(graph,V,src):
    dist = [9999]*V
    dist[src] = 0
    visited = [False]*V
    for _ in range(V):
        u = min_distance(V,dist,visited)
        visited[u] = True
        for i in range(V):
            if graph[u][i] > 0 and visited[i] == False and dist[i]>dist[u]+graph[u][i]:
                dist[i] = dist[u]+graph[u][i]
    print("vertex\tDistance from source:")
    for node in range(V):
        print(node,"\t\t",dist[node])
n=int(input("Enterv no of vertices: "))
print("Enter the adjacent matrix:") 
g=[]
for i in range(n):
    data = list(map(int,input().split(" ")))
    g.append(data)
s=int(input("Enter the source matrix:"))
dijkstra(g,n,s)