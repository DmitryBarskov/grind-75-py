class Solution:
    """
    >>> Solution().isValid("()")
    True
    >>> Solution().isValid("()[]{}")
    True
    >>> Solution().isValid("(]")
    False
    >>> Solution().isValid("([])")
    True
    """

    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(':
                stack.append(')')
            elif char == '[':
                stack.append(']')
            elif char == '{':
                stack.append('}')
            else:
                if len(stack) == 0 or stack[-1] != char:
                    return False
                stack.pop()
        return len(stack) == 0
