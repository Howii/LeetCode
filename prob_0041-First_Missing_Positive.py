def firstMissingPositive(nums: list) -> int:
    nums = [x for x in nums if x > 0]
    s = set(range(1, len(nums) + 2))
    for i in nums:
        if i in s:
            s.remove(i)
    res = min(s)
    return res
