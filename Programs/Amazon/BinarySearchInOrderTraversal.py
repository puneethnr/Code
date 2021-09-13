# In Order travesal/DFS. Visti all the nodes to the left first, then the root and the one to the right
from Data_Structures.BinarySearchTrees.BinarySearchTree import (
    BinarySearchTree
)
from Data_Structures.Utilities.BinarySearchTreeNode import BinarySearchTreeNode

def inOrderTraversal(binarySeachTree: BinarySearchTree):
    elements = []
    'For In order traversal we do a DFS search by passing in a queue into the recursion which stores values as we traverse.'
    traverseTree(binarySeachTree.rootNode, elements)
    print(elements)


def traverseTree(btreeNode:BinarySearchTreeNode, elements):
    if btreeNode is None:
        return

    traverseTree(btreeNode.leftSubNode, elements)
    elements.append(btreeNode.key)
    traverseTree(btreeNode.rightSubNode, elements)



root = BinarySearchTreeNode("M", 123)
root.leftSubNode = BinarySearchTreeNode("K", 234)
root.rightSubNode = BinarySearchTreeNode("R", 234)
binarySearchTree = BinarySearchTree(root)
inOrderTraversal(binarySearchTree)
