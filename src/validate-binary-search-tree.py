from typing import Optional

from tree_node import TreeNode
# pylint: disable=wrong-import-order

from math import inf
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    >>> Solution().isValidBST(TreeNode.from_list([2,1,3]))
    True
    >>> Solution().isValidBST(TreeNode.from_list([5,1,4,None,None,3,6]))
    False
    """
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.recur(root, -inf, inf)

    def recur(self, root: Optional[TreeNode], min_value: float, max_value: float) -> bool:
        if root is None:
            return True
        return min_value < root.val < max_value and \
            self.recur(root.left, min_value, root.val) and \
            self.recur(root.right, root.val, max_value)
