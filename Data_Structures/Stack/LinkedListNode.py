"""
Class to represent a linked list note
"""

class LinkedListNode:

    def __init__(self, item, next):
        """Item within the Node"""
        self.item = item
        """Pointer to the next Node"""
        self.nextNode = next

    def getNode(self):
        return self.nextNode
