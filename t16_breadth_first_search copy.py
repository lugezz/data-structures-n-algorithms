"""
Breadth FS = Traverse a graph level by level
Utilizes a Queue
Better if destination is on average close to start
Siblings are visited before children

Depth FS   = Traverse a graph branch by branch
Utilizes a Stack
Better if destination is on average far from the start
Children are visited before siblings
More popular for games/puzzles
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

    def breadth_first_search(self, src: int):
        """Performs breadth-first search starting from the given source node."""
        from collections import deque

        visited = [False] * len(self.nodes)
        queue = deque([src])
        visited[src] = True

        while queue:
            src = queue.popleft()
            print(f"{self.nodes[src].data} = visited")

            for i in range(len(self.matrix[src])):
                if self.matrix[src][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True


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

# Check breadth-first search
print("-" * 50)
print("Breadth First Search starting from node A:")
# Start BFS from node A (index 0)
# Expected output: A, B, C, D, E
graph.breadth_first_search(0)

print("-" * 50)
print("Breadth First Search starting from node B:")
# Start BFS from node B (index 1)
# Expected output: B, C, E, D, A
graph.breadth_first_search(1)

print("-" * 50)
print("Breadth First Search starting from node D:")
# Start BFS from node D (index 3)
# Expected output: D
graph.breadth_first_search(3)
