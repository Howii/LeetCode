def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    nums.sort()
    cur_sum = sum(nums[:3])
    cur_min = abs(cur_sum - target)
    for i in range(len(nums) - 2):
        j, k = i + 1, len(nums) - 1
        while j < k:
            s = nums[i] + nums[j] + nums[k]
            if s == target:
                return s
            if abs(s - target) < cur_min:
                cur_min = abs(s - target)
                cur_sum = s
            if s < target:
                j += 1
            elif s > target:
                k -=1
    return cur_sum
