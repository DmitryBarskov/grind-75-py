from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        >>> Solution().twoSum([2,7,11,15], 9)
        [0, 1]
        >>> Solution().twoSum([3,2,4], 6)
        [1, 2]
        >>> Solution().twoSum([3,3], 6)
        [0, 1]
        """
        met_before = {}
        for i, num in enumerate(nums):
            if target - num in met_before:
                return [met_before[target - num], i]
            met_before[num] = i
        return None
