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

### Second idea

import bisect

def threeSumClosest2(nums, target):
    nums.sort()
    current_sum = sum(nums[:3])
    current_dif = abs(current_sum - target)
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            partial = nums[i] + nums[j]

            k = bisect.bisect_left(nums, target - partial, j + 1)
            k = min(k, len(nums) - 1)
            tmp_sum = partial + nums[k]
            tmp_dif = abs(tmp_sum - target)
            if tmp_dif < current_dif:
                print("ge", (i, j, k),
                      (nums[i], nums[j], nums[k]),
                      tmp_sum)
                current_dif = tmp_dif
                current_sum = tmp_sum

            k = max(k - 1, j + 1)
            tmp_sum = partial + nums[k]
            tmp_dif = abs(tmp_sum - target)
            if tmp_dif < current_dif:
                print("lt", (i, j, k),
                      (nums[i], nums[j], nums[k]),
                      tmp_sum)
                current_dif = tmp_dif
                current_sum = tmp_sum

            if current_dif == 0:
                return current_sum

    return current_sum

### Test Cases

case = [-1,0,1,1,55]
target = 3

x = threeSumClosest2(case, target)
print(x)

