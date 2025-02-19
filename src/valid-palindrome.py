class Solution:
    """
    >>> Solution().isPalindrome("A man, a plan, a canal: Panama")
    True
    >>> Solution().isPalindrome("race a car")
    False
    >>> Solution().isPalindrome(" ")
    True
    """
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if i >= j:
                break
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
