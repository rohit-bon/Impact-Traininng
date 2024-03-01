import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
        # print(self.graph)
    
    def min_key(self, key, mst_set):
        min_val = sys.maxsize
        
        for v in range(self.V):
            if key[v] < min_val and mst_set[v] == False:
                min_val = key[v]
                min_index = v
        
        return min_index
    
    def print_mst(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])
    
    def prim_mst(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        # print(parent)
        key[0] = 0
        mst_set = [False] * self.V
        print(mst_set)
        parent[0] = -1
        
        for cout in range(self.V):
            u = self.min_key(key, mst_set)
            mst_set[u] = True
            
            for v in range(self.V):
                if self.graph[u][v] > 0 and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    # print(key[v])
                    parent[v] = u
                    # print(parent[v])
        
        self.print_mst(parent)

#Example usage:
g = Graph(6)
g.graph = [
    [0,2,3,0,0,0],
    [2,0,5,3,0,0],
    [3,5,0,0,4,0],
    [0,3,0,0,2,3],
    [0,0,0,2,0,5],
    [0,0,0,3,5,0]
]
g.prim_mst()