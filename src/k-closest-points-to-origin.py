from typing import Callable, Generic, List, TypeVar

T = TypeVar("T")

class MyHeap(Generic[T]):
    """
    >>> min_heap = MyHeap(lambda x, y: x - y)
    >>> len(min_heap)
    0
    >>> min_heap.push(42)
    >>> len(min_heap)
    1
    >>> min_heap.push(37)
    >>> min_heap.heap
    [37, 42]
    """

    __slots__ = 'compare_fn', 'heap'

    def __init__(self, compare: Callable[[T, T], float]):
        self.compare_fn: Callable[[T, T], float] = compare
        self.heap: List[T] = []

    def __len__(self):
        return len(self.heap)

    def push(self, item: T):
        self.heap.append(item)
        self.__sift_up(len(self) - 1)

    def __sift_up(self, start: int):
        current: int = start
        while current > 0 and self.__lt(current, (current - 1) // 2):
            self.__swap(current, (current - 1) // 2)
            current = (current - 1) // 2

    def pop(self) -> T:
        popped: T = self.heap[0]
        self.__swap(0, len(self) - 1)
        self.heap.pop()
        self.__sift_down(0)
        return popped

    def __sift_down(self, start: int):
        current: int = start
        while True:
            left: int = 2 * current + 1
            right: int = 2 * current + 2
            least: int = current
            if left < len(self) and self.__lt(left, least):
                least = left
            if right < len(self) and self.__lt(right, least):
                least = right
            if current == least:
                break
            self.__swap(current, least)
            current = least

    def __lt(self, i1: int, i2: int) -> bool:
        return self.compare_fn(self.heap[i1], self.heap[i2]) < 0

    def __swap(self, i1: int, i2: int):
        self.heap[i1], self.heap[i2] = self.heap[i2], self.heap[i1]


class Solution:
    """
    >>> Solution().kClosest([[1,3],[-2,2]], 1)
    [[-2, 2]]
    >>> sorted(Solution().kClosest([[3,3],[5,-1],[-2,4]], 2))
    [[-2, 4], [3, 3]]
    >>> sorted(Solution().kClosest([[0,1],[1,0]], 2))
    [[0, 1], [1, 0]]
    """

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap: MyHeap[List[int]] = MyHeap(
            lambda a, b: Solution.__distance_sqr(a) - Solution.__distance_sqr(b)
        )
        for point in points:
            min_heap.push(point)
        # print(min_heap.heap)
        return [min_heap.pop() for _ in range(k)]

    @staticmethod
    def __distance_sqr(point: List[int]) -> float:
        x, y = point
        return x * x + y * y
