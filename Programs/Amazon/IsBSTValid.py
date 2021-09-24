
from Data_Structures.BinarySearchTrees.BinarySearchTree import (
    BinarySearchTree
)
from Data_Structures.Utilities.BinarySearchTreeNode import BinarySearchTreeNode

def isBSTValid(binartSearchTree):
    return valid(binartSearchTree, float("-inf"), float("inf"))

def valid(node, left, right):
    if node is None:
        return True

    if not (node.value > left and node.value < right):
        return False

    return valid(node.left, left, node.value) and valid(node.right, node.value, right)


def isBSTValidInOrderTraversal(binartSearchTree):
    q  = []
    return valid(binartSearchTree, q)

def valid(node, q):
    if node is None:
        return True
    lenght = len(q)
    if lenght > 1 and not (q[lenght-1] > q[lenght - 2]):
        return False

    leftRes = valid(node.leftSubNode, q)
    q.append(node.value)
    rightRes = valid(node.rightSubNode, q)
    return leftRes and rightRes

# root = BinarySearchTreeNode("M", 123)
# root.leftSubNode = BinarySearchTreeNode("K", 120)
# root.rightSubNode = BinarySearchTreeNode("R", 234)
# print(isBSTValid(root))

root = BinarySearchTreeNode("M", 123)
root.leftSubNode = BinarySearchTreeNode("K", 120)
root.leftSubNode.leftSubNode = BinarySearchTreeNode("K", 100)
root.leftSubNode.rightSubNode = BinarySearchTreeNode("K", 121)
root.rightSubNode = BinarySearchTreeNode("R", 234)
print(isBSTValidInOrderTraversal(root))