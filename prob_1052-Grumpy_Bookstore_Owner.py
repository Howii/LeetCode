from typing import List

def maxSatisfied(customers: List[int], grumpy: List[int], minutes: int):
    baseline = sum((c for c, g in zip(customers, grumpy) if g == 0))
    potentials = [c if g == 1 else 0 for c, g in zip(customers, grumpy)]
    
    tmp = sum(potentials[:minutes])
    top = tmp
    for j in range(minutes, len(potentials)):
        i = j - minutes
        tmp += potentials[j] - potentials[i]
        if tmp > top:
            top = tmp

    return baseline + top

## Test
customers = [1,0,1,2,1,1,7,5]
grumpy    = [0,1,0,1,0,1,0,1]
minutes   = 3
print(maxSatisfied(customers, grumpy, minutes))
