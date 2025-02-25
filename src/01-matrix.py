from typing import List
from collections import deque

class Solution:
    """
    >>> Solution().updateMatrix([[0,0,0],[0,1,0],[0,0,0]])
    [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    >>> Solution().updateMatrix([[0,0,0],[0,1,0],[1,1,1]])
    [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
    """
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue: deque = deque()
        for i, row in enumerate(mat):
            for j, cell in enumerate(row):
                if cell != 0:
                    continue
                queue.append((i, j, 0))
        return self.__bfs(len(mat), len(mat[0]), queue)

    def __bfs(self, rows: int, columns: int, queue: deque) -> List[List[int]]:
        distance_to_zero: List[List[int]] = [[20_002] * columns for row in range(rows)]
        while len(queue) > 0:
            i, j, dist = queue.popleft()
            if dist >= distance_to_zero[i][j]:
                continue
            distance_to_zero[i][j] = dist
            for r, c in [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]:
                if r < 0 or rows <= r or c < 0 or columns <= c:
                    continue
                queue.append((r, c, dist + 1))
        return distance_to_zero
