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

    def __init__(self, compare: Callable[[T, T], int]):
        self.compare_fn: Callable[[T, T], int] = compare
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
    >>> Solution().findKthLargest([3,2,1,5,6,4], 2)
    5
    >>> Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4)
    4
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap: MyHeap = MyHeap(lambda x, y: y - x)
        for num in nums:
            max_heap.push(num)
        for _ in range(k - 1):
            kth_largest = max_heap.pop()
        return max_heap.pop()
