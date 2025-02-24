from typing import Callable

bad_version: int = 1

def set_bad_version(version: int):
    # pylint: disable-next=global-statement
    global bad_version
    bad_version = version

def isBadVersion(version: int) -> bool:
    return version >= bad_version

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    """
    >>> set_bad_version(4)
    >>> Solution().firstBadVersion(5)
    4
    >>> set_bad_version(1)
    >>> Solution().firstBadVersion(1)
    1
    """

    def firstBadVersion(self, n: int) -> int:
        return self.binary_search(1, n, isBadVersion)

    def binary_search(self, start: int, end: int, predicate: Callable[[int], bool]) -> int:
        lo = start
        hi = end
        while lo < hi:
            mi = (lo + hi) // 2
            if predicate(mi):
                hi = mi
            else:
                lo = mi + 1
        return lo
