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
            for k in range(m*n-1) :
                if self[k]>self[k+1] :
                    grid.swap(self[k],self[k+1])

#Ici, la complexité vaut 2(mn)!, qui représente le cas où la grid est rangée dans l'ordre décroissant.

import matplotlib.pyplot as plt

def graphique(Self) :
    plt.show()

import heapq

def A_star(self, src, dst):
    if egal_matrices(src, dst):
        return "Même source et destination"
    else:
        Solution = Grid(grid.m, grid.n).grid_as_tuple()
        Queue = [(0, src)]  # Tuple de priorité et de grille
        Visited = set()  # Ensemble de grilles visitées
        Parent = {}  # Dictionnaire de grilles parents
        Found = False

        while Queue and not Found:
            # Extraire la grille avec la plus petite priorité de la file de priorité
            _, Current_grid = heapq.heappop(Queue)

            if Current_grid not in Visited:
                Visited.add(Current_grid)

                # Trouver les grilles adjacentes à la grille actuelle
                Next_grids = Grid(len(Current_grid), len(Current_grid[0]), Current_grid).adjacent_grids()

                for (N, swap) in Next_grids:
                    # Calculer la priorité : coût actuel + estimation du coût restant
                    priority = len(Parent) + len(Solver.get_solution(N))
                    
                    if N not in Parent or priority < Parent[N][0]:
                        Parent[N] = (priority, Current_grid, swap)
                        heapq.heappush(Queue, (priority, N))

                    if N == Solution:
                        Found = True

        # Reconstruire le chemin
        path = []
        N = Solution
        while N != src:
            _, N, swap = Parent[N]
            path.append(swap)
        path.reverse()
        return path