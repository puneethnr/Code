from BinarySearchTree import BinarySearchTree

#Test the class
def testBinarySearchTree():
	binarySearchTree = BinarySearchTree(None);         
	print("Result of Searching for 10 in BST:")
	print(binarySearchTree.get(10))
	assert binarySearchTree.get(10) == None


testBinarySearchTree();	