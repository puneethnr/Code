# Level Order travesal/DFS. Visti all the nodes to the left first, then the root and the one to the right
from Data_Structures.BinarySearchTrees.BinarySearchTree import (
    BinarySearchTree
)
from Data_Structures.Utilities.BinarySearchTreeNode import BinarySearchTreeNode

def levelOrderTraversal(binarySeachTree: BinarySearchTree):
    traverseTree(binarySeachTree)


def traverseTree(btreeNode:BinarySearchTreeNode):
    'for levelOrderTraversal we keep a queue, traverse through each node and it to the queue
    elements = []
    if btreeNode is None:
        return

    elements.append(btreeNode)

    while len(elements) > 0:
        currentNode = elements.pop(0)
        print(currentNode.key)
        if currentNode.leftSubNode is not None:
            elements.append(currentNode.leftSubNode)
        if currentNode.rightSubNode is not None:
            elements.append(currentNode.rightSubNode)


root = BinarySearchTreeNode("M", 123)
root.leftSubNode = BinarySearchTreeNode("K", 234)
root.rightSubNode = BinarySearchTreeNode("R", 234)
levelOrderTraversal(root)
