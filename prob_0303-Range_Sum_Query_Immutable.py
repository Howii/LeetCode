class NumArray:

    def __init__(self, nums: list):
        self.nums = nums
        self.cums = {-1 : 0}

    def cumSum(self, idx: int):
        if idx not in self.cums:
            self.cums[idx] = self.nums[idx] + self.cumSum(idx - 1)
        return self.cums[idx]
        
    def sumRange(self, left: int, right: int) -> int:
        return self.cumSum(right) - self.cumSum(left - 1)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
