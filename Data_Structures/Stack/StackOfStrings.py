from Data_Structures.Stack.StackInterface import StackInterface
from Data_Structures.Stack.LinkedListNode import (
    LinkedListNode,
)


class StackOfStrings(StackInterface):

    firstNode = None

    def push(self, item):
        oldFirst = self.firstNode
        self.firstNode = LinkedListNode(item, oldFirst)

    def pop(self):
        value = self.firstNode.item
        self.firstNode = self.firstNode.nextNode
        return value

    def isEmpty(self):
        if self.firstNode is None:
            return True
        else:
            return False




