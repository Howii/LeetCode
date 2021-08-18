CODES = set(str(x) for x in range(1, 27))

## Divide and Conquer
def numDecodings(s: str) -> int:   
    if not s:
        return 1
    elif s[0] == "0":
        return 0
    elif len(s) == 1:
        return 1
    
    mid = len(s) // 2
    left = s[:mid]
    right = s[mid:]
    
    out = numDecodings(left) * numDecodings(right)
    
    middle = s[(mid-1):(mid+1)]
    if middle in CODES:
        left = s[:(mid-1)]
        right = s[(mid+1):]
        out += numDecodings(left) * numDecodings(right)
    
    return out
