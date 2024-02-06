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

import matplotlib.pyplot as plt

def graphique(Self) :
    plt.show()
