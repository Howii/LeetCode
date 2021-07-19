LEFT, RIGHT = "(", ")"

def parenthesisHelper(s, p, q):
    """
    :type s: str, starting string 
    :type p: int, no. remaining left parenthesis
    :type q: int, no. remaining right parenthesis
    :rtype: List[str]
    Invariant: 0 <= p <= q
    """
    if p == 0:
        return [s + [RIGHT] * q]
    elif p == q:
        return parenthesisHelper(s + [LEFT], p - 1, q)
    else:
        tmp1 = parenthesisHelper(s + [LEFT], p - 1, q)
        tmp2 = parenthesisHelper(s + [RIGHT], p, q - 1)
        return tmp1 + tmp2

def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    if n == 0:
        return [""]
    return ["".join(x) for x in parenthesisHelper([LEFT], n - 1, n)]
