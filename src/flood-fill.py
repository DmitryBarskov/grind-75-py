from typing import List

class Solution:
    """
    >>> Solution().floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)
    [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    >>> Solution().floodFill([[0,0,0],[0,0,0]], 0, 0, 0)
    [[0, 0, 0], [0, 0, 0]]
    """
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        stack: List[tuple[int, int]] = [(sr, sc)]
        while len(stack) > 0:
            r, c = stack.pop()
            if image[r][c] == color:
                continue

            for y, x in self.adjacent(image, r, c):
                if image[y][x] == image[r][c]:
                    stack.append((y, x))
            image[r][c] = color
        return image

    def adjacent(self, image: List[List[int]], sr: int, sc: int) -> List[tuple[int, int]]:
        return [
            (y, x) for y, x in [
                (sr - 1, sc), (sr, sc - 1), (sr + 1, sc), (sr, sc + 1),
            ] if 0 <= y < len(image) and 0 <= x < len(image[y])
        ]
