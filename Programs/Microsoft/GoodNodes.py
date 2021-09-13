'''
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNodes = []
        self.traverseTree(root, [], goodNodes)
        print(len(goodNodes))

    def traverseTree(self, btreeNode: TreeNode, maxElements, goodNodes):
        if btreeNode is None:
            return

        if len(maxElements) > 0:
            maxElement = maxElements[-1]
        else:
             maxElement = btreeNode.val

        if btreeNode.val >= maxElement:
            maxElements.append(btreeNode.val)
            goodNodes.append(btreeNode)
        else:
            maxElements.append(maxElement)

        self.traverseTree(btreeNode.left, maxElements, goodNodes)
        self.traverseTree(btreeNode.right, maxElements, goodNodes)
        maxElements.pop()

solution = Solution()
# tree = TreeNode(3)
# tree.left = TreeNode(1)
# tree.left.left = TreeNode(3)
# tree.right = TreeNode(4)
# tree.right.left = TreeNode(1)
# tree.right.right = TreeNode(5)
# solution.goodNodes(tree)

tree = TreeNode(2)
tree.right = TreeNode(4)
tree.right.left = TreeNode(10)
tree.right.right = TreeNode(8)
tree.right.right.left = TreeNode(4)
solution.goodNodes(tree)