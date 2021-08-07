# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def levelOrder(root):
    if not root:
        return []
    
    current_level = [ root ]
    result = []
    while current_level:
        current_vals = [ node.val for node in current_level ]
        result.append(current_vals)
        next_level = []
        for node in current_level:
            next_level += node.children
        # next_level = [ y for node in current_level for y in node.children ]
        current_level = next_level
    
    return result
