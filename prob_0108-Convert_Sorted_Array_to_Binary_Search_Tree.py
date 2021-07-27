# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums: list) -> TreeNode:
    if len(nums) == 1:
        node = TreeNode(nums[0])
    elif len(nums) == 2:
        node = TreeNode(nums[1])
        node.left = TreeNode(nums[0])
    else:
        middleIdx = len(nums) // 2
        node = TreeNode(nums[middleIdx])
        node.left = sortedArrayToBST(nums[:middleIdx])
        node.right = sortedArrayToBST(nums[(middleIdx + 1):])
    
    return node
