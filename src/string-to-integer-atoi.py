class Solution:
    """
    >>> Solution().myAtoi("")
    0
    >>> Solution().myAtoi("42")
    42
    >>> Solution().myAtoi("   -042")
    -42
    >>> Solution().myAtoi("1337c0d3")
    1337
    >>> Solution().myAtoi("0-1")
    0
    >>> Solution().myAtoi("words and 987")
    0
    >>> Solution().myAtoi(" 2147483647L")
    2147483647
    >>> Solution().myAtoi(" -2147483648L")
    -2147483648
    >>> Solution().myAtoi(" 2147483648L")
    2147483647
    >>> Solution().myAtoi(" -2147483649L")
    -2147483648
    >>> Solution().myAtoi(" + 42")
    0
    >>> Solution().myAtoi(" +42")
    42
    >>> Solution().myAtoi("4294967296")
    2147483647
    """
    char_to_digit = {str(d): d for d in range(0, 10)}

    def myAtoi(self, s: str) -> int:
        return self._parse_int(self._find_int(s))

    def _find_int(self, s: str) -> list:
        """
        >>> Solution()._find_int("42")
        [4, 2]
        """
        # 1. whitespace
        i: int = 0
        while i < len(s) and s[i] == " ":
            i += 1

        # 2. signedness
        num: list = []
        if i < len(s) and s[i] in ("-", "+"):
            num.append(s[i])
            i += 1

        # 3. skip leading zeroes
        while i < len(s) and s[i] == "0":
            i += 1

        # 4. read until non-digit character
        while i < len(s) and s[i] in self.char_to_digit:
            num.append(self.char_to_digit[s[i]])
            i += 1

        if len(num) == 0 or num[-1] in ("-", "+"):
            num.append(0)
        return num

    def _parse_int(self, num: list) -> int:
        """
        >>> Solution()._parse_int([4, 2])
        42
        """
        start: int = 0
        sign: int = 1
        if num[0] in ("-", "+"):
            if num[0] == "-":
                sign = -1
            start = 1

        integer: int = sign * num[start]
        start += 1
        for i in range(start, len(num)):
            if integer == 214748364 and num[i] > 7 or integer > 214748364:
                return 2147483647
            if integer == -214748364 and num[i] > 8 or integer < -214748364:
                return -2147483648
            integer = integer * 10 + sign * num[i]

        return integer
