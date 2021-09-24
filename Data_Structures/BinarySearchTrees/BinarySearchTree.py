"""
Interface for a Queue
"""
from Data_Structures.Utilities.BinarySearchTreeNode import (
    BinarySearchTreeNode
)
from Data_Structures.BinarySearchTrees.BinarySearchTreeInterface import BinarySearchTreeInterface

class BinarySearchTree(BinarySearchTreeInterface):

    def __init__(self, rootNode):
        self.rootNode = rootNode

    def put(self, key, value):
        pass

    def get(self, key):
        pass

    def delete(self, key):
        pass