# Level Order travesal/DFS. Visti all the nodes to the left first, then the root and the one to the right
from Data_Structures.BinarySearchTrees.BinarySearchTree import (
    BinarySearchTree
)
from Data_Structures.Utilities.BinarySearchTreeNode import BinarySearchTreeNode

def levelOrderTraversal(binarySeachTree: BinarySearchTree):
    return traverseTree(binarySeachTree)


def traverseTree(btreeNode:BinarySearchTreeNode):
    'for levelOrderTraversal we keep a queue, traverse through each node and it to the queue'
    elements = []
    if btreeNode is None:
        return
    elements.append(btreeNode)

    i = 0
    while len(elements) > i:
        currentNode = elements[i]
        if currentNode.leftSubNode is not None:
            elements.append(currentNode.leftSubNode)
        if currentNode.rightSubNode is not None:
            elements.append(currentNode.rightSubNode)
        i += 1
    return elements


root = BinarySearchTreeNode("M", 123)
root.leftSubNode = BinarySearchTreeNode("K", 99)
root.rightSubNode = BinarySearchTreeNode("R", 235)
elements = levelOrderTraversal(root)
for i in elements:
    print(i.value)
