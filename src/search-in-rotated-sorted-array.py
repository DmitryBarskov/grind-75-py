from typing import Callable, List

class Solution:
    """
    >>> Solution().search([4,5,6,7,0,1,2], 0)
    4
    >>> Solution().search([4,5,6,7,0,1,2], 3)
    -1
    >>> Solution().search([1], 0)
    -1
    >>> Solution().search([-1, 0, 1, 4, 7, 8, 9, 10], 7)
    4
    >>> Solution().search([10, -1, 0, 1, 4, 7, 8, 9], 7)
    5
    >>> Solution().search([1], 2)
    -1
    """
    def search(self, nums: List[int], target: int) -> int:
        rotation: int = self._binary_search(
                0, len(nums), lambda i: nums[i] < nums[0]
        )
        candidate: int = self._binary_search(
                0, rotation, lambda i: nums[i] >= target
        )
        if candidate < len(nums) and nums[candidate] == target:
            return candidate

        candidate = self._binary_search(
                rotation, len(nums), lambda i: nums[i] >= target
        )
        if candidate < len(nums) and nums[candidate] == target:
            return candidate
        return -1

    def _binary_search(
            self, start: int, end: int, predicate: Callable[[int], bool]
    ) -> int:
        lo = start
        hi = end

        while lo < hi:
            mi = (lo + hi) // 2
            if predicate(mi):
                hi = mi
            else:
                lo = mi + 1
        return lo
