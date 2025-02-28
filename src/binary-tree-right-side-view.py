from typing import Optional, Callable, List

from tree_node import TreeNode

# pylint: disable-next=wrong-import-order
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    >>> null = None
    >>> Solution().rightSideView(TreeNode.from_list([1,2,3,null,5,null,4]))
    [1, 3, 4]
    >>> Solution().rightSideView(TreeNode.from_list([1,2,3,4,null,null,null,5]))
    [1, 3, 4, 5]
    >>> Solution().rightSideView(TreeNode.from_list([1,null,3]))
    [1, 3]
    >>> Solution().rightSideView(TreeNode.from_list([]))
    []
    """

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_side_view: List[int] = []

        def set_level(node, level):
            while len(right_side_view) <= level:
                right_side_view.append(-1)
            right_side_view[level] = node.val

        self.__breadth_first_search(root, set_level)
        return right_side_view

    def __breadth_first_search(
            self, root: Optional[TreeNode], callback: Callable[[TreeNode, int], None]
    ) -> None:
        queue: deque = deque([(root, 0)])
        while len(queue) > 0:
            node, depth = queue.popleft()
            if node is None:
                continue
            callback(node, depth)
            queue.append((node.left, depth + 1))
            queue.append((node.right, depth + 1))
