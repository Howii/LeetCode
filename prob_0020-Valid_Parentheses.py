def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    left  = ("(", "[", "{")
    right = (")", "]", "}")
    match = dict(zip(left, right))
    stack = []
    for c in s:
        if c in left:
            stack.append(c)
        if c in right:
            if not stack or match[stack.pop()] != c:
                return False
    return not stack
