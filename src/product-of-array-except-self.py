from typing import List

class Solution:
    """
    >>> Solution().productExceptSelf([1,2,3,4])
    [24, 12, 8, 6]
    >>> Solution().productExceptSelf([-1,1,0,-3,3])
    [0, 0, 9, 0, 0]
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # for nums = [ 1,  2, 3, 4]
        # prefix   = [ 1,  1, 2, 6]
        # suffix   = [24, 12, 4, 1]
        # result[i] = prefix[i] * suffix[i]
        prefix = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        suffix = [1] * len(nums)
        for i in reversed(range(0, len(nums) - 1)):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        return [prefix[i] * suffix[i] for i in range(len(nums))]
