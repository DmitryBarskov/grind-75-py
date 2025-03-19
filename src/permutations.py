from typing import List

class Solution:
    """
    >>> sorted(Solution().permute([1, 2, 3]))
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

    >>> sorted(Solution().permute([0, 1]))
    [[0, 1], [1, 0]]

    >>> Solution().permute([1])
    [[1]]
    """

    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        permutations: List[List[int]] = []
        for i, num in enumerate(nums):
            for permutation in self.permute(nums[:i] + nums[i + 1:]):
                permutation.append(num)
                permutations.append(permutation)
        return permutations
