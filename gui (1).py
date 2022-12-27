from tkinter import *
import customtkinter
import tkintermapview
import ast
from BFS import *
from DFS import *
from UCS import *
from a_star import *
# reading the data from the file
with open('Coordinates.txt') as f:
    data = f.read()
# reconstructing the data as a dictionary
Coordinates = ast.literal_eval(data)
with open('graph.txt') as f:
    data = f.read()
graph = ast.literal_eval(data)
with open('Graph (1).txt') as f:
    data = f.read()
graph2 = ast.literal_eval(data)

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")
root = customtkinter.CTk()
root.title("Distance Between cities in delta")
root.state('zoomed')

frame3 = customtkinter.CTkFrame(master=root)
frame1=customtkinter.CTkFrame(master=frame3)
frame2=customtkinter.CTkFrame(master=frame3)
Cities=[]
for i in Coordinates:
    Cities.append(i)
start=customtkinter.CTkOptionMenu(frame1, values=Cities)
destination=customtkinter.CTkOptionMenu(frame2,values=Cities)
lfrom=customtkinter.CTkLabel(master=frame1,text="From:",font=customtkinter.CTkFont(size=20, weight="bold"))
lto=customtkinter.CTkLabel(master=frame2,text="To:",font=customtkinter.CTkFont(size=20, weight="bold"))
frame1.pack(anchor=W, side = LEFT,padx=200)
frame2.pack(anchor=E, side = RIGHT,padx=200)
frame3.pack(pady=50)
lfrom.pack(side= LEFT, padx=10)
start.pack(side=LEFT)
start.set("Choose your start point")
destination.set("Choose your destination point")
lto.pack(side=LEFT , padx=10)
destination.pack(side=RIGHT)
map_widget= tkintermapview.TkinterMapView(root , width=800,height=400)
map_widget.set_position(30.5784722 ,31.1461905 )
map_widget.set_zoom(9)
map_widget.pack()
frame4=customtkinter.CTkFrame(master=root)
frame4.pack(pady=10)
def clear():
   for i in range(len(map_widget.canvas_marker_list) - 1, -1, -1):
        map_widget.canvas_marker_list[i].delete()
   for i in range(len(map_widget.canvas_path_list) - 1, -1, -1):
        map_widget.canvas_path_list[i].delete()
   text = " "
   distance.configure(text=text)

def input_start():
  a=start.get()
  return a

def input_destination():
   b=destination.get()
   return b

def draw_map(city ):
    clear()
    marker = map_widget.set_marker(Coordinates[city[0]][0], Coordinates[city[0]][1] ,text=city[0] , font=customtkinter.CTkFont(size=15, weight="bold") )

    for i in city[1:] :
       latitude= Coordinates[i][0]
       longitude= Coordinates[i][1]
       marker1 = map_widget.set_marker(latitude,longitude,text=i,font=customtkinter.CTkFont(size=15, weight="bold"))
       path_1 = map_widget.set_path([marker.position, marker1.position])
       marker=marker1
def cost(path):
    cost = 0
    i = 1
    for x in path:
        for y in graph[x]:
            if (y == path[i]):
                cost = cost + graph.get(x).get(y)
        i = i + 1
        if (i == len(path)):
            break
    return int(cost)
def bfs_function():
    path=bfs(graph ,input_start(),input_destination())
    draw_map(path)
    x =cost(path)
    distance.configure(text="Distance =" + str(x)+" km",font=customtkinter.CTkFont(size=15, weight="bold"))

def dfs_function():
    path = dfs(graph, input_start(), input_destination())
    draw_map(path)
    x = cost(path)
    distance.configure(text="Distance =" + str(x)+" km",font=customtkinter.CTkFont(size=15, weight="bold"))
def a_star_function():
    path= A_star(graph2 ,input_start(),input_destination())
    draw_map(path)
    x=cost(path)
    distance.configure(text="Distance =" + str(x)+" km",font=customtkinter.CTkFont(size=15, weight="bold"))

def ucs_function():
    path=(ucs(graph2,input_start(),input_destination()))
    draw_map(path)
    x = cost(path)
    distance.configure(text="Distance =" + str(x)+" km",font=customtkinter.CTkFont(size=15, weight="bold"))

a_star_button = customtkinter.CTkButton(master=frame4 , text="A-star",command=a_star_function)
a_star_button.pack(pady=10, padx=10,side=LEFT)
bfs_button = customtkinter.CTkButton(master=frame4 , text="BFS" ,command=bfs_function)
bfs_button.pack(pady=10, padx=10,side=LEFT)
dfs_button = customtkinter.CTkButton(master=frame4 , text="DFS",command=dfs_function)
dfs_button.pack(pady=10, padx=10,side=LEFT)

ucs_button = customtkinter.CTkButton(master=frame4 , text="UCS",command=ucs_function)
ucs_button.pack(pady=10, padx=10,side=LEFT)
clear_button = customtkinter.CTkButton(master=frame4 , text="Clear",command=clear)
clear_button.pack(pady=10, padx=10,side=RIGHT)
distance=customtkinter.CTkLabel(master=root,text=" ")
distance.pack()
root.mainloop()



