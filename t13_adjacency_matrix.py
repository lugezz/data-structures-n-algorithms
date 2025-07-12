"""
Adjacency Matrix = An array to store 1's/0's to represent edges
of rows =    # of unique nodes
of columns = # of unique nodes

runtime complexity to check an Edge: O(1)
space complexity: O(v^2)
"""


class Graph:
    """ A simple implementation of a graph using an adjacency matrix. """
    def __init__(self, size):
        """ Initializes the graph with a given size. """
        self.nodes = []
        self.matrix = [[0] * size for _ in range(size)]

    def add_node(self, node):
        """ Adds a node to the graph. """
        if len(self.nodes) >= len(self.matrix):
            raise ValueError("Graph is full — cannot add more nodes.")
        self.nodes.append(node)

    def add_edge(self, src: int, dst: int):
        """ Adds an edge between two nodes in the graph. """
        self.matrix[src][dst] = 1

    def check_edge(self, src: int, dst: int) -> bool:
        """ Checks if there is an edge between two nodes. """
        return self.matrix[src][dst] == 1

    def print(self):
        """ Prints the adjacency matrix of the graph. """
        print("  ", end="")
        for node in self.nodes:
            print(node.data, "", end="")
        print("  ")

        for i in range(len(self.matrix)):
            print(self.nodes[i].data, "", end="")
            for j in range(len(self.matrix[i])):
                print(self.matrix[i][j], "", end="")
            print("  ")


class Node:
    """ A simple node class for the graph. """
    def __init__(self, data):
        """ Initializes a node with the given data. """
        self.data = data


graph = Graph(5)

nodes_list = ['A', 'B', 'C', 'D', 'E']

for node_data in nodes_list:
    graph.add_node(Node(node_data))

graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(2, 4)
graph.add_edge(4, 0)
graph.add_edge(4, 2)
graph.print()

check1 = graph.check_edge(0, 1)  # Should return True
print(f"Edge from A to B: {check1}")
check2 = graph.check_edge(1, 3)  # Should return False
print(f"Edge from B to D: {check2}")
