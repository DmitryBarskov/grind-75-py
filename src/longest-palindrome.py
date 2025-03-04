from collections import Counter

class Solution:
    """
    >>> Solution().longestPalindrome("abccccdd")
    7
    >>> Solution().longestPalindrome("a")
    1
    >>> Solution().longestPalindrome("aa")
    2
    >>> Solution().longestPalindrome("Aa")
    1
    """
    def longestPalindrome(self, s: str) -> int:
        letters_count: Counter = Counter(s)
        is_odd_palindrome: bool = False
        longest_palindrome: int = 0
        for count in letters_count.values():
            longest_palindrome += count - count % 2
            if count % 2 == 1 and not is_odd_palindrome:
                is_odd_palindrome = True
                longest_palindrome += 1
        return longest_palindrome
