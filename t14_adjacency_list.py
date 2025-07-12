"""
Adjacency List = An array/arraylist of linkedlists.
Each LinkedList has a unique node at the head.
All adjacent neighbors to that node are added to that node's linkedlist

runtime complexity to check an Edge: O(v)
space complexity: O(v + e)
"""


class Graph:
    """ A simple implementation of a graph using an adjacency list. """
    def __init__(self):
        """ Initializes the graph with an empty adjacency list. """
        self.nodes = []
        self.alist = []

    def add_node(self, node):
        """ Adds a node to the list and expands the adjacency list. """
        self.nodes.append(node)
        # Expand the adjacency list to accommodate the new node
        self.alist.append([])

    def add_edge(self, src: int, dst: int):
        """ Adds an edge between two nodes in the graph. """
        if src < len(self.alist) and dst < len(self.alist):
            if dst not in self.alist[src]:
                self.alist[src].append(dst)

    def check_edge(self, src: int, dst: int) -> bool:
        """ Checks if there is an edge between two nodes. """
        if src < len(self.alist) and dst < len(self.alist):
            return dst in self.alist[src]
        return False

    def print(self):
        """ Prints the adjacency list of the graph. """
        for i, node in enumerate(self.nodes):
            print(f"{node.data} -> ", end="")
            for neighbor in self.alist[i]:
                print(f"{self.nodes[neighbor].data} -> ", end="")
            print()


class Node:
    """ A simple node class for the graph. """
    def __init__(self, data):
        """ Initializes a node with the given data. """
        self.data = data


graph = Graph()

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
