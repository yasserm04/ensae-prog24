"""
This is the grid module. It contains the Grid class and its associated methods.
"""

# On importe ce dont on a besoin, notamment permutations pour la question 6

import random
import numpy as np
from itertools import permutations
from graph import Graph
from queue import Queue
import matplotlib.pyplot as plt

class Grid():
    """
    A class representing the grid from the swap puzzle. It supports rectangular grids. 

    Attributes: 
    -----------
    m: int
        Number of lines in the grid
    n: int
        Number of columns in the grid
    state: list[list[int]]
        The state of the grid, a list of list such that state[i][j] is the number in the cell (i, j), i.e., in the i-th line and j-th column. 
        Note: lines are numbered 0..m and columns are numbered 0..n.
    """
    
    def __init__(self, m, n, initial_state = []):
        """
        Initializes the grid.

        Parameters: 
        -----------
        m: int
            Number of lines in the grid
        n: int
            Number of columns in the grid
        initial_state: list[list[int]]
            The intiail state of the grid. Default is empty (then the grid is created sorted).
        """
        self.m = m
        self.n = n
        if not initial_state:
            initial_state = [list(range(i*n+1, (i+1)*n+1)) for i in range(m)]            
        self.state = initial_state

    def __str__(self): 
        """
        Prints the state of the grid as text.
        """
        output = f"The grid is in the following state:\n"
        for i in range(self.m): 
            output += f"{self.state[i]}\n"
        return output

    def __repr__(self): 
        """
        Returns a representation of the grid with number of rows and columns.
        """
        return f"<grid.Grid: m={self.m}, n={self.n}>"

    def is_sorted(self):
        """
        Checks is the current state of the grid is sorte and returns the answer as a boolean.
        """
        # TODO: implement this function (and remove the line "raise NotImplementedError").
        for k in range (self.m) :
            for l in range (self.n-1) :
                if self.state[k][l]>self.state[k][l+1] :
                    return False
        for k in range (self.m-1)    
            if self.state[k][self.n]>self.state[k+1][0] :
                return False
        return True

    """La complexité est de l'ordre de O(2mn), car on effectue mn actions avec les for, et à chaque fois on effectue une vérification supplémentaire avec if"""

    def swap(self, cell1, cell2):
        """
        Implements the swap operation between two cells. Raises an exception if the swap is not allowed.

        Parameters: 
        -----------
        cell1, cell2: tuple[int]
            The two cells to swap. They must be in the format (i, j) where i is the line and j the column number of the cell. 
        """
        # TODO: implement this function (and remove the line "raise NotImplementedError").
        (i1,j1) = cell1
        (i2,j2) = cell2
        if (i1==i2 and abs(j1-j2)==1) or (j1==j2 and abs(i1-i2)==1) :
            (self.state[i1][j1],self.state[i2][j2])=(self.state[i2][j2],self.state[i1][j1])
        else :
            raise ValueError("Les cellules ne sont pas voisines")

    def swap_seq(self, cell_pair_list):
        """
        Executes a sequence of swaps. 

        Parameters: 
        -----------
        cell_pair_list: list[tuple[tuple[int]]]
            List of swaps, each swap being a tuple of two cells (each cell being a tuple of integers). 
            So the format should be [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...].
        """
        # TODO: implement this function (and remove the line "raise NotImplementedError").
        for(cell1,cell2) in cell_pair_list :
            self.swap(cell1,cell2)

    @classmethod
    def grid_from_file(cls, file_name): 
        """
        Creates a grid object from class Grid, initialized with the information from the file file_name.
        
        Parameters: 
        -----------
        file_name: str
            Name of the file to load. The file must be of the format: 
            - first line contains "m n" 
            - next m lines contain n integers that represent the state of the corresponding cell

        Output: 
        -------
        grid: Grid
            The grid
        """
        with open(file_name, "r") as file:
            m, n = map(int, file.readline().split())
            initial_state = [[] for i_line in range(m)]
            for i_line in range(m):
                line_state = list(map(int, file.readline().split()))
                if len(line_state) != n: 
                    raise Exception("Format incorrect")
                initial_state[i_line] = line_state
            grid = Grid(m, n, initial_state)
        return grid


"""Question 4"""

def representation_graphique(self):
    grille = np.array(self.state)
    plt.matshow(grille)
# Renvoie une matrice, où chaque couleur représente un chiffre en particulier de la grille

"""Question 6 :
Les listes ne sont pas de type hashable.
On peut alors transformer chaque grille en un tuple, qui est immuable
On peut créer représenter toutes les formes possibles de la grille en trouvant toutes les permutations"""

def grid_as_tuple (self) : # pour renvoyer la grille en tant que tuple, on sait jamais
    L = []
    for k in range (len(self.state)) :
        L.append(tupple(self.state[k])) :
    L = tuple (L)
    return L

def noeuds (self) :
    (m,n) = = (self.m,self.n)
    liste = [k for k in range(1, m*n+1)] # on crée la liste de tous les nombres contenus dans la grille
    perm = tuple (permutations (liste)) # on prend toutes les permutations possibles, sous forme de tuple ce qui les rend hashables
    total = []
    for k in perm:
        k = (np.array(k)).reshape((m, n))
        k = tuple(tuple(element) for element in k) # il faut que tout soit hashable
        total.append(k)
    return total # renvoie une liste contenant toutes les grilles (qui sont des tuples de tuples)


"""Question 7 :
Pour générer tous les nœuds, on effectue une permutation sur une liste de taille m*n, aboutissant ainsi à (mn)! nœuds.

Dans une grille de dimension mn, il est possible d'effectuer m*(n-1) échanges
entre des cases adjacentes horizontalement et n*(m-1) échanges entre des cases adjacentes verticalement.
Ainsi, chaque grille a m*(n-1) + n*(m-1) voisins.

Si deux noeuds sont reliés, alors ils le sont via une unique arête.
Par conséquent, le nombre total d'arêtes est donné par (m*n)! * (m(n-1) + n(m-1)) / 2.

Concernant la complexité de l'algorithme BFS :

Dans le pire scénario, nécessitant le parcours de tous les sommets du graphe, la complexité est en O((m*n)!).
Cette complexité est considérablement plus élevée que celle de la méthode naïve.
De plus, l'algorithme BFS appliqué aux grilles utilise la fonction liste_noeuds_voisins, avec une complexité de l'ordre O((mn)!^3 * (mn)^2),
et a donc une complexité encore plus élevée.

Voici les fonctions ajoutées pour appliquer la méthode bfs :"""

"""Fonction 1 : pour voir si deux listes de listes de même dimension sont égales, pour traiter le cas où src = dst"""
def egal_matrices(G1,G2) :
    for k in range (np.shape(G1)[0]) :
        for l in range (np.shape(G1)[1]) :
            if G1[k][l] != G2[k][l] :
                return False
        return True

"""Fonction 2 : permet de vérifier si un couple de listes de listes est présent
dans un une liste de couples de listes de listes"""

def dans_liste(G1,G2, liste) :
    for (k,l) in liste :
        if egal_matrices(G1,k) and egal_matrices(Gé,l) :
            return True
    return False

"""Fonction 3 : pour trouver les voisins dans le graphe, renvoie liste des couples voisins"""

def liste_noeuds_voisins(self):
    m = self.m
    n = self.n
    L = []
    for M1 in self.noeuds () :
        M11 = [list (t) for t in M1]
        for M2 in self.noeuds ():
            M21 = [list(t) for t in M2]
            if not egal_matrices(M11, M21):
                if not dans_liste (M11, M21, L) and not Grid.dans_liste (M21, M11, L):
                    if (M1,M2) not in L and (M2,M1) not in L :
                            L.append((M1,M2))
    return L


"""Fonction 4 : méthode BFS pour la grille. Renvoie tous les chemins dans sol
On transforme la grille en un graph pour pouvoir appliquer le bfs de la classe Graph
Puis on choisit le chemin le plus court"""

def chemin_le_plus_court(self, src, dst):
    graphe_grilles = Graph(Grid.noeuds (self))
    for (i, j) in self.liste_noeuds_voisins():
        graphe_grilles.add_edge(i, j) # pour mettre limites au graphe en fonction de la grille
    src = tuple(tuple (element) for element in src)
    dst = tuple(tuple (element) for element in dst)
    solution = graphe_grilles.bfs(self,src, dst)
    sol = [[list(t) for t in G] for G in solution]
    sol2 = []
    k = 0
    while sol2 :
        for j in range(len(sol)) :
            if len(sol[j]) == k :
                sol2.append(sol[j])
            k = k+1
    return sol2

"""Question 8 :
On construit le chemin pendant la recherche, en s'inspirant du premier bfs"""

def nv_bfs(self, src, dst):
    if egal_matrices(src,dst) :
        return "Même source et destination"
    else :    
        queue = [src]
        visited = [] # liste de noeuds visités, différente de la queue
        parents = {} 
        g = {} # on initialise dictionnaire du graphe
        while queue :
            x = queue.pop(0)
            if x == dst:
                break
            if x not in visited :
                if x not in g:
                    g[x] = [] # on crée le dictionnaire au fur et à mesure qu'on en a besoin
                    for (i, j) in liste_noeuds_voisins(self):
                        i1 = [list(t) for t in i]
                        j1 = [list(t) for t in j]
                        if egal_matrices(i1, x):
                            g[x].append(i)
                        elif egal_matrices(j1, x):
                            g[x].append(j)
                visited.append(x)
            for voisin in g[x]:
                if voisin not in visited :
                    queue.append(voisin)
                    parents[voisin] = x
                    visited.append(voisin)
        chemin = [dst]
        y = dst
        while y != src :
            y = parents[y]
            chemin.append(y)
        return chemin[::-1]