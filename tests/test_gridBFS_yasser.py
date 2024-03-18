import sys 
sys.path.append("swap_puzzle/")
from grid import Grid
import random

import unittest 

class Test_GridBFS(unittest.TestCase):
    
    def test_grid_already_sorted(self):
        grid = Grid(3,3,[[1,2,3],[4,5,6],[7,8,9]])
        self.assertEqual([],Grid.nv_bfs2(grid))
    
    def test_grid_one_swap(self):
        grid = Grid(3,3,[[1,2,3],[4,5,6],[7,8,9]])
        i = random.randint(0,1)
        j = random.randint(0,2)
        grid2 = grid.swap((i,j),(i+1,j))
        self.assertEqual([((i,j),(i+1,j))],Grid.nv_bfs2(grid))

if __name__ == '__main__':
    unittest.main()