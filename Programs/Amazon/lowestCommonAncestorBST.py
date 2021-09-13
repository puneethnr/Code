
def lowestCommonAncestor(binarySearchTree, pNode, qNode):

    if binarySearchTree is None:
        return None
    cur = binarySearchTree
    
    while cur:
        if pNode.Value > cur.value and qNode.Value >  cur.value:
            cur = cur.right
        elif pNode.Value < cur.value and qNode.Value <  cur.value:
            cur = cur.left
        else:
            return cur