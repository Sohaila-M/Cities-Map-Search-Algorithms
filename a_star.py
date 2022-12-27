from math import radians, cos, sin, asin, sqrt
import ast
# reading the data from the file
with open('Graph (1).txt') as f:
    data = f.read()
# reconstructing the data as a dictionary
d = ast.literal_eval(data)
# reading the data from the file
with open('Coordinates.txt') as f:
    data = f.read()
# reconstructing the data as a dictionary
Coordinates = ast.literal_eval(data)
# Python 3 program to calculate Distance Between Two Points on Earth
def distance(start , destination ):
    # The math module contains a function named
    # radians which converts from degrees to radians.
    lon1 = radians(Coordinates[start][1])
    lon2 = radians(Coordinates[destination][1])
    lat1 = radians(Coordinates[start][0])
    lat2 =radians(Coordinates[destination][0])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2

    c = 2 * asin(sqrt(a))

    # Radius of earth in kilometers. Use 3956 for miles
    r = 6371

    # calculate the result
    return (c * r)
cities=[]
H_table={}
for i in Coordinates :
    cities.append(i)

def fill_H_table(destination):
    for city in cities :
        H_table[city] = distance(city,destination)
def path_f_cost(path):
    g_cost=0
    for(node,cost)in path:
        g_cost+=cost
    last_node=path[-1][0]
    h_cost=H_table[last_node]
    f_cost=g_cost+h_cost
    return f_cost,last_node
def a_star_search(graph,start,goal):
    fill_H_table(goal)
    visited=[]
    queue = [[(start,0)]]
    while queue:
        queue.sort(key=path_f_cost)
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
def A_star(graph,start,goal):
    solution=[ ]
    path=a_star_search(graph,start,goal)
    for city in path :
        solution.append(city[0])
    return solution


