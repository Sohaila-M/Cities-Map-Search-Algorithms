from math import radians, cos, sin, asin, sqrt
import ast
# reading the data from the file
with open('Graph (1).txt') as f:
    data = f.read()
# reconstructing the data as a dictionary
d = ast.literal_eval(data)
def path_cost(path):
    g_cost=0
    for(node,cost)in path:
        g_cost+=cost
    last_node=path[-1][0]
    return g_cost,last_node
def ucs_search(graph,start,goal):
    visited=[]
    queue = [[(start,0)]]
    while queue:
        queue.sort(key=path_cost)
        path=queue.pop(0)
        node=path[-1][0]
        if node in visited:
            continue
        visited.append(node)
        if node==goal:
            return path
        else:
            adjacent_nodes=graph.get(node,[])
            for(node2,cost) in adjacent_nodes:
                new_path=path.copy()
                new_path.append((node2,cost))
                queue.append(new_path)
def ucs(graph,start,goal):
    solution=[ ]
    path=ucs_search(graph,start,goal)
    for city in path :
        solution.append(city[0])
    return solution

