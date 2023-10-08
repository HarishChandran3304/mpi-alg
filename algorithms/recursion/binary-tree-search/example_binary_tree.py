## EXAMPLE BINARY TO TEST PARALLEL BINARY TREE SEARCH

# Binary Tree Class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Creating the nodes
node0 = TreeNode(0)
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)
node9 = TreeNode(9)
node10 = TreeNode(10)
node11 = TreeNode(11)
node12 = TreeNode(12)
node13 = TreeNode(13)
node14 = TreeNode(14)

# Building the Binary Tree
node0.left = node1
node0.right = node2
node1.left = node3
node1.right = node4
node2.left = node5
node2.right = node6
node3.left = node7
node3.right = node8
node4.left = node9
node4.right = node10
node5.left = node11
node5.right = node12
node6.left = node13
node6.right = node14

root = node0