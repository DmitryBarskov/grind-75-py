from collections import deque
from typing import Callable, List, Optional

from tree_node import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    >>> null = None
    >>> Solution().levelOrder(TreeNode.from_list([3,9,20,null,null,15,7]))
    [[3], [9, 20], [15, 7]]
    >>> Solution().levelOrder(TreeNode.from_list([1]))
    [[1]]
    >>> Solution().levelOrder(TreeNode.from_list([]))
    []
    """

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels: List[List[int]] = []
        def add_to_level(node: TreeNode, level: int):
            while level >= len(levels):
                levels.append([])
            levels[level].append(node.val)

        self.__bfs(root, add_to_level)
        return levels

    def __bfs(self, root: Optional[TreeNode], callback: Callable[[TreeNode, int], None]):
        queue: deque[tuple[Optional[TreeNode], int]] = deque()
        queue.append((root, 0))
        while len(queue) > 0:
            node, level = queue.popleft()
            if node is None:
                continue
            callback(node, level)
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))
