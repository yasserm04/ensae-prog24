import sys 
sys.path.append("swap_puzzle/")
from graph import Graph

import unittest 

class Test_GraphBFS(unittest.TestCase):
    
    def test_graph1(self):
        g = Graph.graph_from_file("input/graph1.in")
        file = open("input/graph1.path.out", "r")
        lines = file.readlines()
        for line in lines:
            Newline = line.split(" ")
            src, dst = Newline[0], Newline[1]
            path = g.bfs(int(src),int(dst))
            if path is None:
                Generated_line = src + ' ' + dst + ' None\n'
            else:
                Generated_line = src + ' ' + dst + ' ' + str(len(path) - 1) + ' ' + str(path) + '\n'
            self.assertEqual(Generated_line.strip(), line.strip())
        file.close()

    def test_graph2(self):
        g = Graph.graph_from_file("input/graph2.in")
        file = open("input/graph2.path.out", "r")
        lines = file.readlines()
        for line in lines:
            Newline = line.split(" ")
            src, dst = Newline[0], Newline[1]
            path = g.bfs(int(src),int(dst))
            if path is None:
                Generated_line = src + ' ' + dst + ' None\n'
            else:
                Generated_line = src + ' ' + dst + ' ' + str(len(path) - 1) + ' ' + str(path) + '\n'
            self.assertEqual(Generated_line.strip(), line.strip())
        file.close()



if __name__ == '__main__':
    unittest.main()