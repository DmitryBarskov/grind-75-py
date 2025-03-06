from typing import List

class Solution:
    """
    >>> Solution().coinChange([1,2,5], 11)
    3
    >>> Solution().coinChange([2], 3)
    -1
    >>> Solution().coinChange([1], 0)
    0
    >>> Solution().coinChange([1,2,3,4,5], 10000)
    2000
    >>> Solution().coinChange([1, 6, 7, 9, 11], 13)
    2
    """

    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coins: List[int] = [-1] * (amount + 1)
        min_coins[0] = 0
        for i, _ in enumerate(min_coins):
            if min_coins[i] == -1:
                continue
            for coin_value in coins:
                next_amount: int = i + coin_value
                if next_amount >= len(min_coins):
                    continue
                if min_coins[next_amount] == -1:
                    min_coins[next_amount] = min_coins[i] + 1
                min_coins[next_amount] = min(min_coins[next_amount], min_coins[i] + 1)
        return min_coins[amount]
