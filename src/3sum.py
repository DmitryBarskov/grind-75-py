from typing import List

class Solution:
    """
    >>> sorted(Solution().threeSum([-1,0,1,2,-1,-4]))
    [[-1, -1, 2], [-1, 0, 1]]
    >>> sorted(Solution().threeSum([0,1,1]))
    []
    >>> sorted(Solution().threeSum([0,0,0]))
    [[0, 0, 0]]
    >>> sorted(Solution().threeSum([-3, 3, 4, -3, 1, 2]))
    [[-3, 1, 2]]
    >>> sorted(Solution().threeSum([-2,0,0,2,2]))
    [[-2, 0, 2]]
    >>> sorted(Solution().threeSum([2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4]))
    [[-4, 2, 2], [-3, 1, 2], [-2, 0, 2]]
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        triplets = []
        for i in range(len(sorted_nums)):
            if i > 0 and sorted_nums[i - 1] == sorted_nums[i]:
                continue
            j = i + 1
            k = len(sorted_nums) - 1
            while j < k:
                while j < k and j > i + 1 and sorted_nums[j - 1] == sorted_nums[j]:
                    j += 1
                while j < k and k < len(sorted_nums) - 1 and sorted_nums[k] == sorted_nums[k + 1]:
                    k -= 1
                if j >= k:
                    break
                sum = sorted_nums[i] + sorted_nums[j] + sorted_nums[k]
                if sum > 0:
                    k -= 1
                elif sum < 0:
                    j += 1
                else:
                    triplets.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])
                    j += 1
                    k -= 1

        return triplets
