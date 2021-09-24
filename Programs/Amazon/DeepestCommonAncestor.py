
def dcaBST(root, node1, node2):

    cur = root
    while cur:
        if node1.value < cur.left.value and node2.value < cur.left.value:
            cur = cur.left
        elif node1.value > cur.left.value and node2.value > cur.left.value:
            cur = cur.right
        else:
            return cur

def dca(root, node1, node2):
    if root is None:
        return None
    if node1.value == root.value or node2.value == root.value:
        return root

    left = dca(root.left, node1, node2)
    right = dca(root.right, node1, node2)

    if left is not None and right is not None:
        return root

    if left is None and right is None:
        return null

    if left is not None:
        return left
    else:
        return right