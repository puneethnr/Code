from Data_Structures.Queues.QueueInterface import QueueInterface
from Data_Structures.Utilities.LinkedListNode import (
    LinkedListNode,
)


"""
Implementation of a queue of strings
"""

class QueueOfStrings(QueueInterface):

    firstNode = None
    lastNode = None

    def enqueue(self, item):
        # Gather the current first node
        oldLastNode = self.lastNode
        # Update first node to be a new node pointing to the previous first node
        self.lastNode = LinkedListNode(item, None)
        if self.isEmpty():
            self.firstNode = self.lastNode
        else:
            oldLastNode.nextNode = self.lastNode

    def dequeue(self):
        # Gather the value in the first node
        value = self.firstNode.item

        # Update first node to be next node.
        self.firstNode = self.firstNode.nextNode
        if self.isEmpty(): self.lastNode = None

        # Return the value that was stored from the previous first node
        return value

    def isEmpty(self):
        if self.firstNode is None:
            return True
        else:
            return False




