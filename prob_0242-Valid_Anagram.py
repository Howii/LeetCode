from collections import defaultdict

def isAnagram(s: str, t: str) -> bool:
    count = defaultdict(int)
    for i in s:
        count[i] += 1
    for i in t:
        count[i] -= 1
    for c in count.values():
        if c != 0:
            return False
    return True
