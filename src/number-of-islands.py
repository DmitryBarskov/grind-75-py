from typing import List

class Solution:
    """
    >>> Solution().numIslands([
    ...     ["1","1","1","1","0"],
    ...     ["1","1","0","1","0"],
    ...     ["1","1","0","0","0"],
    ...     ["0","0","0","0","0"]
    ... ])
    1
    >>> Solution().numIslands([
    ...     ["1","1","0","0","0"],
    ...     ["1","1","0","0","0"],
    ...     ["0","0","1","0","0"],
    ...     ["0","0","0","1","1"]
    ... ])
    3
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        islands: int = 0
        for i, row in enumerate(grid):
            for j, _ in enumerate(row):
                islands += self._islands_in_cell(grid, i, j)
        return islands

    def _islands_in_cell(self, grid: List[List[str]], row: int, col: int) -> int:
        if not 0 <= row < len(grid) or not 0 <= col < len(grid[row]):
            return 0
        if grid[row][col] == "0":
            return 0
        grid[row][col] = "0"
        self._islands_in_cell(grid, row + 1, col)
        self._islands_in_cell(grid, row - 1, col)
        self._islands_in_cell(grid, row, col + 1)
        self._islands_in_cell(grid, row, col - 1)
        return 1
