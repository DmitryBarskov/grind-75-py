from typing import List

class Solution:
    """
    >>> Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    6
    >>> Solution().maxSubArray([1])
    1
    >>> Solution().maxSubArray([5,4,-1,7,8])
    23
    >>> Solution().maxSubArray([-1])
    -1
    """
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        sum_so_far = 0
        for num in nums:
            sum_so_far = max(sum_so_far, 0)
            sum_so_far += num
            max_sum = max(max_sum, sum_so_far)
        return max_sum
