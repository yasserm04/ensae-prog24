from grid import Grid

class Solver(): 
    """
    A solver class, to be implemented.
    """
    
    def get_solution(self):
        """
        Solves the grid and returns the sequence of swaps at the format 
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 
        """
        # TODO: implement this function (and remove the line "raise NotImplementedError").
        # NOTE: you can add other methods and subclasses as much as necessary. The only thing imposed is the format of the solution returned.
        while is_sorted(self) == False :
            X = []
            for k in range(self.m) :
                for l in range(self.n-1)
                    if self[k][l]>self[k+1][l] :
                        grid.swap(self[k][l],self[k+1][l])
                        X.append(((k,l),(k+1,l)))
            for k in range(self.m-1) :
                if self.state[k][self.n]>self.state[k+1][0] :`
                grid.swap(self[k][self.n],self[k+1][0])
                        X.append(((k,self.n),(k+1,0)))
        return X

import matplotlib.pyplot as plt

def graphique(Self) :
    plt.show()

import heapq
from grid import Grid

def heuristic(self, src, dst):
    objectif = {}
    for i in range(len(dst)):
        for j in range(len(dst[0])):
            num = dst[i][j]
            goal_positions[num] = (i, j)
    
    distance = 0
    for i in range(len(src)):
        for j in range(len(src[0])):
            current_num = src[i][j]
            goal_pos = goal_positions[current_num]
            distance += abs(i - goal_pos[0]) + abs(j - goal_pos[1])
    return distance

# J'utilise la distance de Manhattan : ce n'est pas la plus sophistiquée mais je n'ai pas trouvé comment utiliser la borne inf 


def a_star(grid):
    src = grid.grid_as_tuple()
    dst = Grid(grid.m, grid.n).grid_as_tuple()  # src de même taille
    open_list = [(Solver.heuristic(src, dst), 0, src, [])]
    heapq.heapify(open_list) #transforme en un tas

    visited = {src: 0}

    while open_list:
    heur, cost, current_state, moves = heapq.heappop(open_list)

        if current_state == dst:
            return moves

        for next_grid, swap in grid.liste_noeuds_voisins():
            next_state = next_grid.grid_as_tuple()
            next_cost = cost + 1
                
            if next_state not in visited or next_cost < visited[next_state]:
                visited[next_state] = next_cost
                priority = next_cost + Solver.heuristic(next_state, dst)
                heapq.heappush(open_list, (priority, next_cost, next_state, moves + [swap]))

    raise ValueError("Pas de chemin")
