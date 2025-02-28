class Solution:
    """
    >>> Solution().lengthOfLongestSubstring("abcabcbb")
    3
    >>> Solution().lengthOfLongestSubstring("bbbbb")
    1
    >>> Solution().lengthOfLongestSubstring("pwwkew")
    3
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        met_one_time = set()
        met_more_times = {}
        longest = 0
        l = 0
        for r, char in enumerate(s):
            if char in met_one_time:
                if char not in met_more_times:
                    met_more_times[char] = 0
                met_more_times[char] += 1
            else:
                met_one_time.add(char)

            while len(met_more_times) > 0:
                if s[l] in met_more_times: 
                    met_more_times[s[l]] -= 1
                    if met_more_times[s[l]] == 0:
                        met_more_times.pop(s[l])
                else:
                    met_one_time.remove(s[l])
                l += 1

            longest = max(longest, r - l + 1)
        return longest
