from collections import Counter, deque
from typing import Dict

class Window:
    __slots__ = ('required', 'missing', 'extra', 'window')

    def __init__(self, t: str):
        self.required: Counter = Counter(t)
        self.missing: Dict[str, int] = dict(self.required)
        self.extra: Dict[str, int] = {}
        self.window: deque[str] = deque()

    def add_char(self, char: str):
        self.window.append(char)
        if char not in self.required:
            return

        if char in self.missing:
            self.missing[char] -= 1
            if self.missing[char] <= 0:
                self.missing.pop(char)
        elif char in self.extra:
            self.extra[char] += 1
        else:
            self.extra[char] = 1

    def pop_char(self):
        char: str = self.window.popleft()
        if char not in self.required:
            return

        if char in self.missing:
            self.missing[char] += 1
        elif char in self.extra:
            self.extra[char] -= 1
            if self.extra[char] == 0:
                self.extra.pop(char)
        else:
            self.missing[char] = 1

    def is_included(self) -> bool:
        return len(self.missing) == 0

    def __len__(self):
        return len(self.window)


class Solution:
    """
    >>> Solution().minWindow(s = "ADOBECODEBANC", t = "ABC")
    'BANC'
    >>> Solution().minWindow(s = "a", t = "a")
    'a'
    >>> Solution().minWindow(s = "a", t = "aa")
    ''
    >>> Solution().minWindow("aaaaaaaaaaaabbbbbcdd", "abcdd")
    'abbbbbcdd'
    """

    def minWindow(self, s: str, t: str) -> str:
        window: Window = Window(t)
        shortest: None | tuple[int, int, int] = None
        for i, char in enumerate(s):
            window.add_char(char)
            while window.is_included():
                # pylint: disable-next=unsubscriptable-object
                if shortest is None or len(window) < shortest[2]:
                    shortest = (i - len(window) + 1, i + 1, len(window))
                window.pop_char()
        if shortest is None:
            return ""
        return s[shortest[0]:shortest[1]]
