from typing import List

class Solution:
    """
    >>> Solution().insert([[1,3],[6,9]], [2,5])
    [[1, 5], [6, 9]]
    >>> Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])
    [[1, 2], [3, 10], [12, 16]]
    >>> Solution().insert([[1,5]], [2, 3])
    [[1, 5]]
    >>> Solution().insert([[3,5],[8,10]], [1, 2])
    [[1, 2], [3, 5], [8, 10]]
    """
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        after_insertion: List[List[int]] = []

        i = 0
        # step 1: copy intervals before newInterval
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            after_insertion.append(intervals[i])
            i += 1

        # step 2: add newInterval and merge intersecting intervals
        after_insertion.append(newInterval)
        while i < len(intervals) and self.are_intersecting(after_insertion[-1], intervals[i]):
            after_insertion[-1] = self.merge_intervals(after_insertion[-1], intervals[i])
            i += 1

        # step 3: copy intervals after newInterval
        while i < len(intervals):
            after_insertion.append(intervals[i])
            i += 1

        return after_insertion

    def are_intersecting(self, interval_1: List[int], interval_2: List[int]) -> bool:
        a, b = interval_1
        c, d = interval_2
        return a <= c <= b or a <= d <= b or c <= a <= d or c <= b <= d

    def merge_intervals(self, interval_1: List[int], interval_2: List[int]) -> List[int]:
        return [min(interval_1[0], interval_2[0]), max(interval_1[1], interval_2[1])]
