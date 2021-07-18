def twoSum(nums, target):
    cache = dict()
    for i, num in enumerate(nums):
        if num in cache:
            return( [cache[num][0], i] )
        else:
            cache[target - num] = (i, num)
