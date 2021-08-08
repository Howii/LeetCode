def missingNumber(nums) -> int:
    sum1 = sum2 = 0
    for i, n in enumerate(nums):
        sum1 += i + 1
        sum2 += n
    return sum1 - sum2
