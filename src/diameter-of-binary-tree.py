from typing import Optional

from tree_node import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self._recur(root)[0] - 1

    def _recur(self, root: Optional[TreeNode]) -> tuple[int, int]:
        """
        returns (diameter, height) for given root
        """
        if root is None:
            return (0, 0)
        left_diameter, left_height = self._recur(root.left)
        right_diameter, right_height = self._recur(root.right)
        diameter = max(left_diameter, right_diameter, left_height + 1 + right_height)
        height = max(left_height, right_height) + 1
        return (diameter, height)
