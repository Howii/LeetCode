from typing import List
from collections import defaultdict

def numIdenticalPairs(nums: List[int]) -> int:
    count = defaultdict(int)
    for n in nums:
        count[n] += 1
    res = 0
    for val in count.values():
        if val > 1:
            res += int(val * (val - 1) / 2)
    return res
