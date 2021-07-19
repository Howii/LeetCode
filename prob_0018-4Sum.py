from collections import defaultdict
from itertools import product, combinations_with_replacement

def fourSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    count_table = defaultdict(int)
    for n in nums:
        count_table[n] += 1
    two_sum_table = defaultdict(set)
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            s = nums[i] + nums[j]
            two_sum_table[s].add((nums[i], nums[j]))
    res = []
    for k in two_sum_table.keys():
        c = target - k
        if k > c or c not in two_sum_table:
            continue
        if k < c:
            pairs = product(two_sum_table[k], two_sum_table[target - k])
        else:
            pairs = combinations_with_replacement(two_sum_table[k], 2)
        for a, b in pairs:
            tmp = tuple(sorted(list(a + b)))
            if tmp in res:
                continue
            cnt = defaultdict(int)
            to_append = True
            for n in tmp:
                cnt[n] += 1
                if cnt[n] > count_table[n]:
                    to_append = False
                    break
            if to_append:
                res.append(tmp)
    return [list(x) for x in res]
