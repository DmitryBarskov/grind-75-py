class Solution:
    """
    >>> Solution().climbStairs(2)
    2
    >>> Solution().climbStairs(3)
    3
    >>> Solution().climbStairs(4)
    5
    >>> Solution().climbStairs(5)
    8
    >>> Solution().climbStairs(6)
    13
    >>> Solution().climbStairs(45)
    1836311903
    """
    def climbStairs(self, n: int) -> int:
        step = 0
        two_steps = 1
        for _ in range(n):
            step, two_steps = two_steps, step + two_steps
        return two_steps
