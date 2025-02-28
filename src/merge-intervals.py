from typing import List

class Solution:
    """
    >>> Solution().merge([[1,3],[2,6],[8,10],[15,18]])
    [[1, 6], [8, 10], [15, 18]]
    >>> Solution().merge([[1,4],[4,5]])
    [[1, 5]]
    """

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged: List[List[int]] = []
        for interval in sorted(intervals):
            if len(merged) > 0 and self.__are_intersecting(merged[-1], interval):
                merged[-1] = self.__merge(merged[-1], interval)
            else:
                merged.append(interval)
        return merged

    def __are_intersecting(
            self, interval_1: List[int], interval_2: List[int]
    ) -> bool:
        a, b = interval_1
        c, d = interval_2
        return a <= c <= b or a <= d <= b or c <= a <= d or c <= b <= d

    def __merge(
            self, interval_1: List[int], interval_2: List[int]
    ) -> List[int]:
        return [
            min(interval_1[0], interval_2[0]),
            max(interval_1[1], interval_2[1])
        ]
