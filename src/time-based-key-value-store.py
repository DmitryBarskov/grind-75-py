from typing import Callable, Dict, List

class TimeMap:
    """
    >>> obj = TimeMap()
    >>> obj.set('foo', 'bar', 1)
    >>> obj.get('foo', 1)
    'bar'
    >>> obj.get('foo', 3)
    'bar'
    >>> obj.get('foo', 4)
    'bar'
    >>> obj.set('foo', 'bar2', 4)
    >>> obj.get('foo', 4)
    'bar2'
    >>> obj.get('foo', 5)
    'bar2'
    >>> obj.get('foo', 0)
    ''
    >>> obj.get('foo', 2)
    'bar'
    >>> obj.get('baz', 1)
    ''
    >>> print(obj._hash)
    {'foo': [('bar', 1), ('bar2', 4)]}
    """

    __slots__ = ('_hash',)

    def __init__(self):
        self._hash: Dict[str, List[tuple[str, int]]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self._hash:
            self._hash[key] = []
        self._hash[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self._hash:
            return ""
        bucket: List[tuple[str, int]] = self._hash[key]
        index: int = self._binary_search(
            0, len(bucket),
            lambda i: bucket[i][1] > timestamp
        ) - 1
        if not (0 <= index < len(bucket)) or bucket[index][1] > timestamp:
            return ""
        return bucket[index][0]

    def _binary_search(
            self, start: int, end: int, predicate: Callable[[int], bool]
    ) -> int:
        lo: int = start
        hi: int = end
        while lo < hi:
            mi: int = (lo + hi) // 2
            if predicate(mi):
                hi = mi
            else:
                lo = mi + 1
        return lo
