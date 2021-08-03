from collections import defaultdict

def subsetsFromCounts(counts_list):
    if len(counts_list) > 0:
        num, count = counts_list[0]
        subsets_left = [ [num] * c for c in range(count + 1) ]
        subsets_right = subsetsFromCounts(counts_list[1:])
        subsets = [ x + y for x in subsets_left for y in subsets_right ]
        return subsets
    else:
        return [[]]

def subsetsWithDup(nums):
    counts = defaultdict(int)
    for num in nums:
        counts[num] += 1
    counts_list = list(counts.items())
    return subsetsFromCounts(counts_list)

## Test
nums = [1,2,2,3,3,3]
subs = subsetsWithDup(nums)
for sub in subs:
    print(sub)
