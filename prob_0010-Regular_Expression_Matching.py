STAR = "*"
DOT  = "."

def isMatch(self, s: str, p: str) -> bool:
    # Define base cases
    if len(p) == 0:
        return len(s) == 0
    elif len(s) == 0:
        if len(p) > 1 and p[1] == STAR:
            return self.isMatch(s, p[2:])
        else:
            return False

    # Address four cases: a | . | a* | .* |
    sHead = s[0]
    pHead = p[0]
    powerStar = len(p) > 1 and p[1] == STAR
    if pHead != DOT:
        if not powerStar:
            if sHead == pHead:
                if self.isMatch(s[1:], p[1:]):
                    return True
            else:
                return False
        else:
            if self.isMatch(s, p[2:]):
                return True
            elif sHead == pHead:
                if self.isMatch(s[1:], p):
                    return True
            else:
                return False
    else:
        if not powerStar:
            if self.isMatch(s[1:], p[1:]):
                return True
        else:
            if self.isMatch(s, p[2:]):
                return True
            elif self.isMatch(s[1:], p):
                return True

    return False
