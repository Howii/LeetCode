def removeDuplicates(nums: list) -> int:
    if len(nums) <= 1:
        return len(nums)

    curIndex = 0
    curValue = nums[0]
    i = 1
    totalLength = len(nums)
    while i < totalLength:
        if nums[i] == curValue:
            i += 1
            next
        else:
            curIndex += 1
            nums[curIndex] = nums[i]
            curValue = nums[i]
            i += 1
    return curIndex + 1
