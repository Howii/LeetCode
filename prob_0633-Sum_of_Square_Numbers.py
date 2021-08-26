import math

def judgeSquareSum(c: int) -> bool:
    M = math.ceil(math.sqrt(c / 2)) + 1
    for a in range(0, M):
        b = c - a**2
        if b < 0:
            break
        b = math.sqrt(b)
        if b == int(b):
            return True
    return False

## Test
print(judgeSquareSum(118170)) # 123**2 + 321**2
