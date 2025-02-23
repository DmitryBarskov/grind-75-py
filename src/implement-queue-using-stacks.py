class MyQueue:
    """
    >>> obj = MyQueue()
    >>> obj.push(1)
    >>> obj.push(2)
    >>> obj.peek()
    1
    >>> obj.pop()
    1
    >>> obj.empty()
    False
    """

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self.__ensure_out_stack()
        return self.out_stack.pop()

    def peek(self) -> int:
        self.__ensure_out_stack()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return len(self.in_stack) + len(self.out_stack) == 0

    def __ensure_out_stack(self):
        if len(self.out_stack) > 0:
            return
        while len(self.in_stack) > 0:
            self.out_stack.append(self.in_stack.pop())
