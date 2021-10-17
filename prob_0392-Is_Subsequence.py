def isSubsequence(s: str, t: str) -> bool:
    if not s:
        return True
    c = s[0]
    idx = t.find(c)
    if idx == -1:
        return False
    return isSubsequence(s[1:], t[(idx+1):])

## Test
s = 'abc'
t = 'ahbgdc'
print(isSubsequence(s, t))
