from collections import Counter

class Solution:
    """
    >>> Solution().canConstruct("a", "b")
    False
    >>> Solution().canConstruct("aa", "ab")
    False
    >>> Solution().canConstruct("aa", "aab")
    True
    """
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        available = Counter(magazine)
        required = Counter(ransomNote)
        for char in required:
            if required[char] > available[char]:
                return False
        return True
