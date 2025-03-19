from typing import List

class Solution:
    """
    >>> Solution().addBinary(a = "11", b = "1")
    '100'
    >>> Solution().addBinary(a = "1010", b = "1011")
    '10101'
    """

    def addBinary(self, a: str, b: str) -> str:
        i: int = len(a) - 1
        j: int = len(b) - 1
        res: List[str] = []
        carry: int = 0
        while i >= 0 or j >= 0:
            a_bit: int = 1 if i >= 0 and a[i] == '1' else 0
            b_bit: int = 1 if j >= 0 and b[j] == '1' else 0
            res_bit: int = (a_bit + b_bit + carry) % 2
            carry = (a_bit + b_bit + carry) // 2
            res.append(str(res_bit))
            i -= 1
            j -= 1
        if carry >= 1:
            res.append(str(carry))
        return ''.join(reversed(res))
