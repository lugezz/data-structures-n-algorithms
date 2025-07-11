"""
Python Linked List
Last Updated : 14 Feb, 2025
In this article, we will learn about the implementation of a linked list in Python. To implement the linked list in Python,
we will use classes in Python. Now, we know that a linked list consists of nodes and nodes have two elements i.e. data and
a reference to another node. Let's implement the node first.

A linked list is a type of linear data structure similar to arrays. It is a collection of nodes
that are linked with each other. A node contains two things first is data and second is a link that connects
it with another node. Below is an example of a linked list with four nodes and each node contains character data and a
link to another node. Our first node is where head points and we can access all the elements of the linked list using the head.

Singly-Linked-List
Singly Linked List
Creating a linked list in Python
In this LinkedList class, we will use the Node class to create a linked list. The class includes
the following methods:

__init__: Initializes the linked list with an empty head.
insertAtBegin(): Inserts a node at the beginning of the linked list.
insertAtIndex(): Inserts a node at the given index of the linked list.
insertAtEnd(): Inserts a node at the end of the linked list.
remove_node(): Deletes a node by taking data as an argument. It traverses the linked list and
deletes the node if a match is found.
sizeOfLL(): Returns the current size of the linked list.
printLL(): Traverses the linked list and prints the data of each node. printLL() method ensures
the last node is printed by adding a print(current_node.data) after the loop ends. This handles the edge case of
printing the last node.

Creating a Node Class
We have created a Node class in which we have defined a __init__ function to initialize the node
with the data passed as an argument and a reference with None because if we have only one node
then there is nothing in its reference.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


"""
Insertion in Linked List
1. Insertion at Beginning in Linked List
Insertion-at-the-Beginning-of-Singly-Linked-List
Insertion at Beginning in Linked List
Step-by-step Approach:

Create a new node with the given data.
Check if the head of the linked list is empty (i.e., head == None).
If yes, set the new node as the head of the linked list.
If no, proceed to the next step.
Set the next pointer of the new node to the current head.
Make the new node the new head of the linked list.
Return the updated head (which is now the new node).
"""


def insertAtBegin(self, data):
    new_node = Node(data)
    if self.head is None:
        self.head = new_node
        return
    else:
        new_node.next = self.head
        self.head = new_node


"""
2. Insert a Node at a Specific Position in a Linked List
Insertion-at-a-Specific-Position-of-the-Singly-Linked-List-copy
Insert a Node at a Specific Position in a Linked List
Step-by-step Approach:

Create a new_node with the given data, a current_node that is set to the head, and a counter 'position' initialized to 0.
If the index is 0, it means the node should be inserted at the beginning, so call the insertAtBegin() method.
If the index is not 0, run a while loop until:
The current_node is not equal to None, or
The position+1 is not equal to the index.
In each iteration, increment the position by 1 and update current_node to its next node.
When the loop breaks:
If current_node is not None, insert the new_node after the current_node.
If current_node is None, it means the index is not present in the list, so print "Index not present".

# Method to add a node at any index
# Indexing starts from 0.
"""


def insertAtIndex(self, data, index):
    if (index == 0):
        self.insertAtBegin(data)
        return

    position = 0
    current_node = self.head
    while (current_node is not None and position+1 != index):
        position = position+1
        current_node = current_node.next

    if current_node is not None:
        new_node = Node(data)
        new_node.next = current_node.next
        current_node.next = new_node
    else:
        print("Index not present")


"""
3. Insertion in Linked List at End
Insertion-at-the-End-of-Singly-Linked-List
Insertion in Linked List at End
Step-by-step Approach:

Create a new_node with the given data.
Check if the head is an empty node:
If the head is empty, make the new_node the head and return.
If the head is not empty, set current_node to the head.
Traverse the linked list by running a while loop until current_node becomes None, indicating the last node.
Once the loop breaks, insert the new_node after the current_node, which is the last node of the linked list.
"""


def inserAtEnd(self, data):
    new_node = Node(data)
    if self.head is None:
        self.head = new_node
        return

    current_node = self.head
    while (current_node.next):
        current_node = current_node.next

    current_node.next = new_node


"""
Update the Node of a Linked List
This code defines a method called updateNode in a linked list class. It is used to update the value of a node
at a given position in the linked list.


# Update node of a linked list
# at given position
"""


def updateNode(self, val, index):
    current_node = self.head
    position = 0
    if position == index:
        current_node.data = val
    else:
        while (current_node is not None and position != index):
            position = position+1
            current_node = current_node.next

        if current_node is not None:
            current_node.data = val
        else:
            print("Index not present")


"""
Delete Node in a Linked List
1. Remove First Node from Linked List
Deletion-at-beginning-
Remove First Node from Linked List
Steps-by-step approach:

Check if the head of the linked list is None. If it is, return as there are no nodes to remove.
Update the head to point to the next node (self.head = self.head.next), effectively removing the first node from
the linked list.ist.
"""


def remove_first_node(self):
    if self.head is None:
        return

    self.head = self.head.next


"""
2. Remove Last Node from Linked List
Deletion-At-End
Remove Last Node from Linked List
Step-by-step Approach:

Check if the head of the linked list is None. If it is, return as there are no nodes to remove.
Initialize a current_node with self.head to start from the head of the list.
Traverse the linked list using a while loop that continues until current_node.next is None or current_node.next.next
is None. This ensures the loop stops at the second-to-last node.
Once the loop breaks, current_node will be pointing to the second-to-last node.
Set current_node.next to None, effectively removing the last node from the linked list.
"""


def remove_last_node(self):

    if self.head is None:
        return

    curr_node = self.head
    while (curr_node.next is not None and curr_node.next.next is not None):
        curr_node = curr_node.next

    curr_node.next = None


"""
3. Delete a Linked List Node at a given Position
Deletion-specific-At-End--
Delete a Linked List Node at a given Position
Step-by-step Approach:

If the head is None, simply return as there are no nodes to remove.
Initialize a current_node with self.head and a position with 0.
If the position is equal to the index, call the remove_first_node() method.
If the position is not equal to the index, traverse to the node just before the one to be removed using a while loop.
The loop continues until current_node becomes None or position reaches index - 1.
After the loop:
If current_node or current_node.next is None, it means the index is out of range.
If not, bypass the node to be removed by setting current_node.next to current_node.next.next.

# Method to remove at given index
"""


def remove_at_index(self, index):
    if self.head is None:
        return

    current_node = self.head
    position = 0

    if index == 0:
        self.remove_first_node()
    else:
        while current_node is not None and position < index - 1:
            position += 1
            current_node = current_node.next

        if current_node is None or current_node.next is None:
            print("Index not present")
        else:
            current_node.next = current_node.next.next


"""
4. Delete a Linked List Node of a given Data
Step-by-step Approach:

Initialize a current_node with the head of the linked list and run a while loop to traverse the list.
The loop continues until current_node becomes None or the data of the node next to current_node matches the given data.
After the loop:
If current_node is None, it means the node with the given data is not present, so return without making any changes.
If the data next to current_node matches the given data, remove that node by updating current_node.next to
current_node.next.next, effectively bypassing the node to be removed.
"""


def remove_node(self, data):
    current_node = self.head

    # Check if the head node contains the specified data
    if current_node.data == data:
        self.remove_first_node()
        return

    while current_node is not None and current_node.next.data != data:
        current_node = current_node.next

    if current_node is None:
        return
    else:
        current_node.next = current_node.next.next


"""
Linked List Traversal in Python
Step-by-step Approach:

Initialize a current_node with the head of the linked list.
Use a while loop to traverse the linked list, continuing until current_node becomes None.
In each iteration, print the data of the current_node.
After printing, update current_node to the next node in the list by setting current_node to current_node.next.
"""


def printLL(self):
    current_node = self.head
    while current_node:
        print(current_node.data)
        current_node = current_node.next


"""
Get Length of a Linked List in Python
Step-by-step Approach:

Initialize a size counter with 0.
Check if the head is not None. If the head is None, return 0 as the linked list is empty.
Traverse the linked list using a while loop until current_node becomes None.
In each iteration, increment the size by 1.
Once the loop finishes, return the size, which represents the total number of nodes in the linked list.
"""


def sizeOfLL(self):
    size = 0
    if self.head:
        current_node = self.head
        while current_node:
            size = size+1
            current_node = current_node.next
        return size
    else:
        return 0


"""
Example of the Linked list in Python
In this example, After defining the
Node and LinkedList class we have created a linked list named "llist" using the linked
list class and then insert four nodes with character data 'a', 'b', 'c', 'd' and 'g' in
the linked list then we print the linked list using printLL() method linked list class
after that we have removed some nodes using remove methods and then print the linked
list again and we can see in the output that node is deleted successfully. After that,
we also print the size of the linked list.
"""


# Create a Node class to create a node
class Node1:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create a LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    # Method to add a node at the beginning of the LL
    def insertAtBegin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Method to add a node at any index
    # Indexing starts from 0.
    def insertAtIndex(self, data, index):
        if index == 0:
            self.insertAtBegin(data)
            return

        position = 0
        current_node = self.head
        while current_node is not None and position + 1 != index:
            position += 1
            current_node = current_node.next

        if current_node is not None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index not present")

    # Method to add a node at the end of LL
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    # Update node at a given position
    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        while current_node is not None and position != index:
            position += 1
            current_node = current_node.next

        if current_node is not None:
            current_node.data = val
        else:
            print("Index not present")

    # Method to remove first node of linked list
    def remove_first_node(self):
        if self.head is None:
            return

        self.head = self.head.next

    # Method to remove last node of linked list
    def remove_last_node(self):
        if self.head is None:
            return

        # If there's only one node
        if self.head.next is None:
            self.head = None
            return

        # Traverse to the second last node
        current_node = self.head
        while current_node.next and current_node.next.next:
            current_node = current_node.next

        current_node.next = None

    # Method to remove a node at a given index
    def remove_at_index(self, index):
        if self.head is None:
            return

        if index == 0:
            self.remove_first_node()
            return

        current_node = self.head
        position = 0
        while current_node is not None and current_node.next is not None and position + 1 != index:
            position += 1
            current_node = current_node.next

        if current_node is not None and current_node.next is not None:
            current_node.next = current_node.next.next
        else:
            print("Index not present")

    # Method to remove a node from the linked list by its data
    def remove_node(self, data):
        current_node = self.head

        # If the node to be removed is the head node
        if current_node is not None and current_node.data == data:
            self.remove_first_node()
            return

        # Traverse and find the node with the matching data
        while current_node is not None and current_node.next is not None:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

        # If the data was not found
        print("Node with the given data not found")

    # Print the size of the linked list
    def sizeOfLL(self):
        size = 0
        current_node = self.head
        while current_node:
            size += 1
            current_node = current_node.next
        return size

    # Print the linked list
    def printLL(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


# create a new linked list
llist = LinkedList()

# add nodes to the linked list
llist.insertAtEnd('a')
llist.insertAtEnd('b')
llist.insertAtBegin('c')
llist.insertAtEnd('d')
llist.insertAtIndex('g', 2)

# print the linked list
print("Node Data:")
llist.printLL()

# remove nodes from the linked list
print("\nRemove First Node:")
llist.remove_first_node()
llist.printLL()

print("\nRemove Last Node:")
llist.remove_last_node()
llist.printLL()

print("\nRemove Node at Index 1:")
llist.remove_at_index(1)
llist.printLL()

# print the linked list after all removals
print("\nLinked list after removing a node:")
llist.printLL()

print("\nUpdate node Value at Index 0:")
llist.updateNode('z', 0)
llist.printLL()

print("\nSize of linked list:", llist.sizeOfLL())

"""
Output
Node Data
c
a
g
b
d

Remove First Node
Remove Last Node
Remove Node at Index 1

Linked list after removing a node:
a
b

Update node Value
z
b

Size of linked list : 2
"""
