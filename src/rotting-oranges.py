from typing import Callable, List
from collections import deque

class Solution:
    """
    0 - no orange
    1 - fresh orange
    2 - rotten orange
    3 - rotten and checked orange
    >>> Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
    4
    >>> Solution().orangesRotting([[2,1,1],[0,1,1],[1,0,1]])
    -1
    >>> Solution().orangesRotting([[0,2]])
    0
    >>> Solution().orangesRotting([[2,2],[1,1],[0,0],[2,0]])
    1
    """
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten_oranges: List[tuple[int, int]] = self._find_in_grid(
            grid, lambda o: o == 2
        )
        queue: deque = deque([(y, x, 0) for (y, x) in rotten_oranges])
        last_rotted_at: int = 0

        while len(queue) > 0:
            y, x, rotted_at = queue.popleft()
            if grid[y][x] == 3:
                continue
            grid[y][x] = 3
            last_rotted_at = rotted_at
            for i, j in [(y - 1, x), (y, x - 1), (y, x + 1), (y + 1, x)]:
                if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == 1:
                    queue.append((i, j, rotted_at + 1))
        if len(self._find_in_grid(grid, lambda o: o == 1)) > 0:
            return -1
        return last_rotted_at

    def _find_in_grid(
            self, grid: List[List[int]],
            predicate: Callable[[int], bool]
    ) -> List[tuple[int, int]]:
        found: List[tuple[int, int]] = []
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if predicate(cell):
                    found.append((i, j))
        return found
