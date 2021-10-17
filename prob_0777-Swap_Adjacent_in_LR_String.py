def canTransform(start: str, end: str) -> bool:
    # Solution 1
    if len(start) != len(end):
        return False
    start_wox = start.replace('X', '')
    end_wox = end.replace('X', '')
    if start_wox != end_wox:
        return False
    
    return canTransformHelper(start, end)

def canTransformHelper(start: str, end: str) -> bool:
    N = len(start)
    
    i = 0
    x = []
    while i < N:
        if start[i] == 'R':
            x.append(i)
        elif start[i] == 'L':
            break
        i += 1
    
    j = 0
    y = []
    while j < N:
        if end[j] == 'R':
            y.append(j)
        elif end[j] == 'L':
            break
        j += 1
    
    for xx, yy in zip(x, y):
        if xx > yy:
            return False

    if i == N:
        return True

    if i < j:
        return False

    new_end = end[(j+1):]
    if i == j:
        new_start = start[(j+1):]
    else: # i > j
        new_start = start[j:i] + start[(i+1):]

    return canTransformHelper(new_start, new_end)


def canTransform2(start: str, end: str) -> bool:
    # Solution 2
    if len(start) != len(end):
        return False
    start_wox = start.replace('X', '')
    end_wox = end.replace('X', '')
    if start_wox != end_wox:
        return False

    startL = []
    startR = []
    for i, c in enumerate(start):
        if c == 'L':
            startL.append(i)
        elif c == 'R':
            startR.append(i)

    endL = []
    endR = []
    for i, c in enumerate(end):
        if c == 'L':
            endL.append(i)
        elif c == 'R':
            endR.append(i)

    for x, y in zip(startL, endL):
        if x < y:
            return False

    for x, y in zip(startR, endR):
        if x > y:
            return False

    return True

## Test
start = "RXXLRXRXL"
end = "XRLXXRRLX"

tt = canTransform2(start, end)
print(tt)
