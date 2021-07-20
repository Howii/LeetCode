import random

class Solution:

    def __init__(self, nums: list[int]):
       self.original = nums
       self.present = nums.copy()

    def reset(self) -> list[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.present = self.original.copy()
        return self.present

    def shuffle(self) -> list[int]:
        """
        Returns a random shuffling of the array.
        """
        random.shuffle(self.present)
        return self.present

nums = list(range(1, 10))
obj = Solution(nums)
print(obj.present)

param1 = obj.shuffle()
print(param1)

param2 = obj.reset()
print(param2)

param3 = obj.shuffle()
print(param3)
