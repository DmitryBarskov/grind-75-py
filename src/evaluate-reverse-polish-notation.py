from math import trunc
from typing import List

class Solution:
    """
    >>> Solution().evalRPN(["2", "1", "+", "3", "*"])
    9
    >>> Solution().evalRPN(["4", "13", "5", "/", "+"])
    6
    >>> Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
    22
    """
    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: trunc(a / b),
    }

    def evalRPN(self, tokens: List[str]) -> int:
        stack: List[int] = []
        for token in tokens:
            if token in self.operations:
                if len(stack) < 2:
                    raise TypeError
                right_operand = stack.pop()
                left_operand = stack.pop()
                result = self.operations[token](left_operand, right_operand)
                stack.append(result)
            else:
                stack.append(int(token))
        if len(stack) != 1:
            raise TypeError
        return stack[0]
