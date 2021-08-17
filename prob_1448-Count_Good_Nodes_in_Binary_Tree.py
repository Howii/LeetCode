# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodesHelper(self, node: TreeNode, previousMax: int) -> int:
        if not node:
            return 0
        if node.val >= previousMax:
            currentMax = node.val
            foo = 1
        else:
            currentMax = previousMax
            foo = 0

        leftCount = self.goodNodesHelper(node.left, currentMax)
        rightCount = self.goodNodesHelper(node.right, currentMax)
        return foo + leftCount + rightCount
            
    def goodNodes(self, root: TreeNode) -> int:
        return self.goodNodesHelper(root, root.val-1)
