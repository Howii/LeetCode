#!/usr/bin/env python

from typing import List

def grayCode(n: int) -> List[int]:
    if n == 1:
        return [0, 1]
    
    first_half = grayCode(n-1)
    p = 1 << (n-1)
    second_half = [i + p for i in first_half]
    second_half.reverse()
    return first_half + second_half

## Test
print(grayCode(4))
