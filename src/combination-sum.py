from typing import List

class Solution:
    """
    >>> sorted(Solution().combinationSum([2,3,6,7], 7))
    [[2, 2, 3], [7]]
    >>> sorted(Solution().combinationSum([2,3,5], 8))
    [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    >>> Solution().combinationSum([2], 1)
    []
    """

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combination: List[int] = []
        result: List[List[int]] = []

        def recur(next_index: int, combination_sum: int):
            if next_index >= len(candidates) or combination_sum > target:
                return
            if combination_sum == target:
                result.append(combination[:])
                return

            recur(next_index + 1, combination_sum)

            combination.append(candidates[next_index])
            recur(next_index, combination_sum + candidates[next_index])
            combination.pop()

        recur(0, 0)
        return result
