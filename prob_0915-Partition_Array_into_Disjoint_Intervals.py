def partitionDisjoint(nums: list[int]) -> int:
    # cummulative max from beginning
    x = [nums[0]]
    for num in nums[1:-1]:
        if num >= x[-1]:
            x.append(num)
        else:
            x.append(x[-1])
    
    # cummulative min from end
    y = [nums[-1]]
    for num in reversed(nums[1:-1]):
        if num <= y[-1]:
            y.append(num)
        else:
            y.append(y[-1])
    y.reverse()
    
    for i, a, b in zip(range(len(x)), x, y):
        if a <= b:
            return i + 1
    
    return 1
