from grid import Grid
from graph import Graph
import graph

g = Grid(2, 3)
g2 = Grid(2, 3,[[2,1,3],[4,5,6]])

Graph.bfs(Graph,g,g2)

h = Grid(4,4,[[1,2,7,8],[4,5,6,3],[11,13,10,9],[12,14,15,16]])

print(g, h)

data_path = "input/"
file_name = data_path + "grid0.in"

print(file_name)

g = Grid.grid_from_file(file_name)
print(g)
