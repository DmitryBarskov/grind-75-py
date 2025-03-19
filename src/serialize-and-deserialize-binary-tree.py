from typing import List, Generator, Optional

from tree_node import TreeNode

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    """
    >>> null = None
    >>> root = TreeNode.from_list([1,2,3,null,null,4,5])
    >>> Codec().serialize(TreeNode.from_list([1,2,3,null,null,4,5]))
    '(1 (2 . .) (3 (4 . .) (5 . .)))'
    >>> Codec().deserialize('(1 (2 . .) (3 (4 . .) (5 . .)))').to_list()
    [1, 2, 3, 4, 5]
    >>> Codec().serialize(
    ...     TreeNode.from_list(
    ...         [4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,
    ...          0,6,5,null,9,null,null,-1,-4,null,null,null,-2]
    ...     )
    ... )
    '(4 (-7 . .) (-3 (-9 (6 . (-1 . .)) .) (-3 (-6 . .) (-6 (-2 . .) .))))'
    """

    def serialize(self, root: Optional['TreeNode']) -> str:
        """
        Encodes a tree to a single string.
        >>> null = None
        >>> Codec().serialize(TreeNode.from_list([1,2,3,null,null,4,5]))
        '(1 (2 . .) (3 (4 . .) (5 . .)))'
        """
        if root is None:
            return "."
        return f"({root.val} {self.serialize(root.left)} {self.serialize(root.right)})"


    def deserialize(self, data: str) -> Optional['TreeNode']:
        """
        Decodes your encoded data to tree.
        >>> Codec().deserialize('.') is None
        True
        >>> Codec().deserialize('(1 . .)').val
        1
        >>> Codec().deserialize('(1 . .)').left is None
        True
        >>> Codec().deserialize('(1 . .)').right is None
        True
        """
        stack: List[List[int | None | 'TreeNode']] = [[]]
        for token in self._tokenize(data):
            if token == '(':
                stack.append([])
            elif token is None:
                stack[-1].append(None)
            elif isinstance(token, int):
                stack[-1].append(token)
            elif token == ')':
                children = stack.pop()
                if len(children) == 0:
                    continue
                node = TreeNode(children[0])
                node.left = children[1] if len(children) >= 1 else None
                node.right = children[2] if len(children) >= 2 else None
                stack[-1].append(node)
            else:
                raise TypeError(f"Unexpected token {token} with type {type(token)}")
        root: int | 'TreeNode' | None = stack[0][0]
        if not isinstance(root, TreeNode):
            raise TypeError(f"Expected root to be a TreeNode, got {root}")
        return root

    def _tokenize(self, data: str) -> Generator[str | None | int, None, None]:
        """
        >>> list(Codec()._tokenize('(1 . .)'))
        ['(', 1, None, None, ')']
        """
        i = 0
        while i < len(data):
            if data[i] in ('(', ')'):
                yield data[i]
                i += 1
            elif data[i] == '.':
                yield None
                i += 1
            elif data[i] == ' ':
                i += 1
            elif data[i].isnumeric() or data[i] == '-':
                token: List[str] = []
                while i < len(data) and (data[i].isnumeric() or data[i] == '-'):
                    token.append(data[i])
                    i += 1
                yield int(''.join(token))
