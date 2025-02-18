from typing import List

class Solution:
    """
    >>> Solution().maxProfit([7,1,5,3,6,4])
    5
    >>> Solution().maxProfit([7,6,4,3,1])
    0
    """
    def maxProfit(self, prices: List[int]) -> int:
        min_before = prices[0]
        max_profit = 0
        for price in prices:
            max_profit = max(max_profit, price - min_before)
            min_before = min(min_before, price)
        return max_profit
