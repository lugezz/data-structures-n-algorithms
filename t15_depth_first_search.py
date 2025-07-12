from typing import List

"""
Depth First Search = Pick a route, keep going.
If you reach a dead end, or an already visited node,
backtrack to a previous node with unvisited adjacent neighbors
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

    def depth_first_search(self, src: int):
        """Performs depth-first search starting from the given source node."""
        visited = [False] * len(self.nodes)
        self._dfs_helper(src, visited)

    def _dfs_helper(self, src: int, visited: List[bool]):
        """Helper function for depth-first search."""
        if visited[src]:
            # print(f"{self.nodes[src].data} = already visited")
            return

        visited[src] = True
        print(f"Visiting {self.nodes[src].data}")

        for i, is_connected in enumerate(self.matrix[src]):
            if is_connected == 1:
                if not visited[i]:
                    # print(f"Going to {self.nodes[i].data} from {self.nodes[src].data}")
                    self._dfs_helper(i, visited)
                else:
                    pass
                    # print(f"{self.nodes[i].data} = already visited from {self.nodes[src].data}")


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

# Should return True
check1 = graph.check_edge(0, 1)
print(f"Edge from A to B: {check1}")

# Should return False
check2 = graph.check_edge(1, 3)
print(f"Edge from B to D: {check2}")

# Check depth-first search
print("-" * 50)
print("Depth First Search starting from node A:")
# Start DFS from node A (index 0)
# Expected output: A, B, C, D, E
graph.depth_first_search(0)

print("-" * 50)
print("Depth First Search starting from node B:")
# Start DFS from node B (index 1)
# Expected output: B, C, D, E, A
graph.depth_first_search(1)

print("-" * 50)
print("Depth First Search starting from node D:")
# Start DFS from node D (index 3)
# Expected output: D
graph.depth_first_search(3)
