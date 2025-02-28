class MinStack:
    """
    >>> obj = MinStack()
    >>> obj.push(-2)
    >>> obj.push(0)
    >>> obj.push(-3)
    >>> obj.getMin()
    -3
    >>> obj.pop()
    >>> obj.top()
    0
    >>> obj.getMin()
    -2
    """

    __slots__ = ('_mins', '_stack')

    def __init__(self):
        self._mins: list = []
        self._stack: list = []

    def push(self, val: int) -> None:
        if len(self) > 0:
            self._mins.append(min(val, self._mins[-1]))
        else:
            self._mins.append(val)
        self._stack.append(val)

    def pop(self) -> None:
        self._mins.pop()
        self._stack.pop()

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._mins[-1]

    def __len__(self) -> int:
        return len(self._stack)
