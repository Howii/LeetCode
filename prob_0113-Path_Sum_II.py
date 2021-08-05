# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pathSum(root: TreeNode, targetSum: int) -> list:
    if root:
        val = root.val
        if not root.left and not root.right:
            if val == targetSum:
                return [ [val] ]
            else:
                return []
        
        ret = []
        if root.left:
            leftPaths = pathSum(root.left, targetSum - val)
            if leftPaths:
                ret += [ [val] + path for path in leftPaths ]
        
        if root.right:
            rightPaths = pathSum(root.right, targetSum - val)
            if rightPaths:
                ret += [ [val] + path for path in rightPaths ]
        
        return ret
    else:
        return []
