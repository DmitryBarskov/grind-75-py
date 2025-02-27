class Trie:
    """
    >>> obj = Trie()
    >>> obj.insert("apple")
    >>> obj.search("apple")
    True
    >>> obj.search("app")
    False
    >>> obj.startsWith("app")
    True
    >>> obj.insert("app")
    >>> obj.search("app")
    True
    """

    word_end = ""
    __slots__ = ['root']

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        sub_tree = self.root
        for char in word:
            if char not in sub_tree:
                sub_tree[char] = {}
            sub_tree = sub_tree[char]
        sub_tree[self.word_end] = True

    def search(self, word: str) -> bool:
        sub_tree = self.root
        for char in word:
            if char not in sub_tree:
                return False
            sub_tree = sub_tree[char]
        return sub_tree is not None and self.word_end in sub_tree

    def startsWith(self, prefix: str) -> bool:
        sub_tree = self.root
        for char in prefix:
            if char not in sub_tree:
                return False
            sub_tree = sub_tree[char]
        return sub_tree is not None
