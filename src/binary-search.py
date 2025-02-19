from typing import Callable, List

class Solution:
    """
    >>> Solution().search([-1,0,3,5,9,12], 9)
    4
    >>> Solution().search([-1,0,3,5,9,12], 2)
    -1
    >>> Solution().search([-1,0,3,5,9,12], 13)
    -1
    """
    def search(self, nums: List[int], target: int) -> int:
        candidate = Solution.binary_search(0, len(nums), lambda i: nums[i] >= target)
        if candidate >= len(nums) or nums[candidate] != target:
            return -1
        return candidate

    @staticmethod
    def binary_search(start: int, end: int, predicate: Callable[[int], bool]) -> int:
        """
        >>> Solution.binary_search(1, 100, lambda x: x * x >= 49)
        7
        """
        lo = start
        hi = end
        while lo < hi:
            mi = (lo + hi) // 2
            if predicate(mi):
                hi = mi
            else:
                lo = mi + 1
        return lo
