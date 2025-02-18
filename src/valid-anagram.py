class Solution:
    """
    >>> Solution().isAnagram("anagram", "nagaram")
    True
    >>> Solution().isAnagram("rat", "car")
    False
    """
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        # Or just collections.Counter(s)
        for char in s:
            if char not in count:
                count[char] = 0
            count[char] += 1
        for char in t:
            if char not in count:
                return False
            count[char] -= 1
            if count[char] == 0:
                count.pop(char)
        return len(count) == 0
