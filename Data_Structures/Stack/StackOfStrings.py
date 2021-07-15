from Data_Structures.Stack.StackInterface import StackInterface
from Data_Structures.Stack.LinkedListNode import (
    LinkedListNode,
)


"""
Implementation of a stack of strings
"""

class StackOfStrings(StackInterface):

    firstNode = None

    def push(self, item):
        # Gather the current first node
        oldFirst = self.firstNode
        # Update first node to be a new node pointing to the previous first node
        self.firstNode = LinkedListNode(item, oldFirst)

    def pop(self):
        # Gather the value in the first node
        value = self.firstNode.item

        # Update first node to be next node.
        self.firstNode = self.firstNode.nextNode

        # Return the value that was stored from the previous first node
        return value

    def isEmpty(self):
        if self.firstNode is None:
            return True
        else:
            return False




