"""
Implementation for a Binary search Tree
"""
from BinarySearchTreeInterface import BinarySearchTreeInterface

class BinarySearchTree(BinarySearchTreeInterface):


    def __init__(self, rootNode):
        self.rootNode = rootNode

    def put(self, key, value):
        pass

    def get(self, key):
        x = self.rootNode
        while x is not None:
            if key < x.key:
                x = x.leftSubNode
            elif key > x.key:
                x = x.rightSubNode
            else:
                return x.value
        return None



    def delete(self, key):
        pass


