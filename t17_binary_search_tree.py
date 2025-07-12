"""
Binary Search Tree = A tree data structure, where each node is greater than it's left child,
but less than it's right.

Benefit: easy to locate a node when they are in this order
Time complexity: best case  O(log n)
Worst case O(n)
Space complexity: O(n)
"""


class Node:
    """ A simple node class for the graph. """
    def __init__(self, data):
        """ Initializes a node with the given data. """
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    """ A simple implementation of a binary search tree. """
    def __init__(self):
        """ Initializes the binary search tree with an empty root. """
        self.root = None

    def insert(self, node: Node):
        """ Inserts a node into the binary search tree. """
        if self.root is None:
            self.root = node
        else:
            self.root = self.insert_helper(self.root, node)

    def insert_helper(self, root: Node, node: Node) -> Node:
        """ Helper function to insert a node into the binary search tree. """
        data = node.data

        if root is None:
            root = node
            return root

        if data < root.data:
            root.left = self.insert_helper(root.left, node)
        else:
            root.right = self.insert_helper(root.right, node)
        return root

    def display(self):
        """ Displays the binary search tree in-order. """
        self.display_helper(self.root)

    def display_helper(self, root: Node):
        """ Helper function to display the binary search tree in-order. """
        if root is not None:
            self.display_helper(root.left)
            print(root.data)
            self.display_helper(root.right)

    def search(self, data: int) -> bool:
        """ Searches for a node with the given data in the binary search tree. """
        return self.search_helper(self.root, data)

    def search_helper(self, root: Node, data: int) -> bool:
        """ Helper function to search for a node with the given data in the binary search tree."""
        if root is None:
            return False

        if root.data == data:
            return True
        elif data < root.data:
            return self.search_helper(root.left, data)
        else:
            return self.search_helper(root.right, data)

    def remove(self, data: int):
        """ Removes a node with the given data from the binary search tree. """
        if self.search(data):
            self.root = self.remove_helper(self.root, data)
            print("New root after removal:", self.root.data if self.root else "None")
        else:
            print(f"Node with data {data} not found in the tree.")

    def remove_helper(self, root: Node, data: int) -> Node:
        """ Helper function to remove a node with the given data from the binary search tree. """
        if root is None:
            return root

        if data < root.data:
            root.left = self.remove_helper(root.left, data)

        elif data > root.data:
            root.right = self.remove_helper(root.right, data)

        else:
            # Node with only one child or no child
            if root.left is None and root.right is None:
                root = None
            elif root.right is not None:
                # Find a successor to replace this node
                root.data = self.successor(root)
                root.right = self.remove_helper(root.right, root.data)
            else:
                # Find a predecessor to replace this node
                root.data = self.predecessor(root)
                root.left = self.remove_helper(root.left, root.data)
            return root

    def successor(self, root: Node) -> int:
        """ Find least value below the right child of this root node"""
        root = root.right
        while root.left is not None:
            root = root.left
        return root.data

    def predecessor(self, root: Node) -> int:
        """find greatest value below the left child of this root node"""
        root = root.left
        while root.right is not None:
            root = root.right
        return root.data


tree = BinarySearchTree()

tree.insert(Node(5))
tree.insert(Node(1))
tree.insert(Node(9))
tree.insert(Node(2))
tree.insert(Node(7))
tree.insert(Node(3))
tree.insert(Node(6))
tree.insert(Node(4))
tree.insert(Node(8))

tree.display()

# Check search functionality
print(tree.search(3))  # Should return True
print(tree.search(10))  # Should return False
