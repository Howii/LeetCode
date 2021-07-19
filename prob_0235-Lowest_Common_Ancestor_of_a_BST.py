# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor(root, p, q):
    if p.val >= q.val:
        return lowestCommonAncestor(root, q, p)
    
    if root.val < p.val:
        return lowestCommonAncestor(root.right, p, q)
    elif root.val > q.val:
        return lowestCommonAncestor(root.left, p, q)
    else:
        return root
