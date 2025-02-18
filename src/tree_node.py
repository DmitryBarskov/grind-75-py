from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __iter__(self):
        return TreeNode.BreadthFirstSearch(self)

    def to_list(self) -> List[int]:
        """
        >>> TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4))).to_list()
        [1, 2, 3, 4]
        >>> TreeNode(1, TreeNode(2, TreeNode(5)), TreeNode(3, TreeNode(4))).to_list()
        [1, 2, 3, 5, 4]
        """
        return list(self)

    def from_list(l: List[int], index=0) -> Optional['TreeNode']:
        """
        >>> TreeNode.from_list([2]).val
        2
        >>> TreeNode.from_list([2]).left is None
        True
        >>> TreeNode.from_list([2]).right is None
        True
        """
        if index >= len(l):
            return None
        return TreeNode(
                l[index],
                TreeNode.from_list(l, index=2 * index + 1),
                TreeNode.from_list(l, index=2 * index + 2)
        )

    class BreadthFirstSearch:
        def __init__(self, root):
            self.queue = deque([root])

        def __next__(self):
            if len(self.queue) == 0:
                raise StopIteration
            popped = self.queue.popleft()
            if popped.left is not None:
                self.queue.append(popped.left)
            if popped.right is not None:
                self.queue.append(popped.right)
            return popped.val
