"""
Class to represent a linked list node
"""

class BinarySearchTreeNode:

    def __init__(self, key, value):
        """Item within the Node"""
        self.key = key
        self.value = value
        """Pointer to the next Node"""
        self.leftSubNode = None
        self.rightSubNode = None
