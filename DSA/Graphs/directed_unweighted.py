def add_node(v1):
    global node_count
    if v1 in nodes:
        print("Node already Exist.")
    else:
        node_count += 1
        nodes.append(v1)
        for p in graph:
            p.append(0)
        temp = []
        for p in range(0,node_count):
            temp.append(0)
        graph.append(temp)
        
def add_edges(v1,v2):
    if v1 not in nodes:
        print(v1, "Node doesn't Exist.")
    elif v2 not in nodes:
        print(v2, "Node doesn't Exist.")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2) 
        graph[index1][index2] = 1

def print_graph():
    for p in range(node_count):
        for q in range(node_count):
            print(graph[p][q],end=" ")
        print()


nodes = []
graph = []
node_count = 0
print("Befor adding")
print(nodes)
print(graph)
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
print(nodes)
print(graph)
print_graph()
add_edges("A","B")
add_edges("A","C")
add_edges("A","D")
add_edges("B","D")
add_edges("B","E")
add_edges("C","D")
add_edges("D","E")
print(nodes)
print(graph)
print_graph()