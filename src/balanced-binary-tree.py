from typing import Optional

from tree_node import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    >>> Solution().isBalanced(TreeNode.from_list([3,9,20,None,None,15,7]))
    True
    >>> Solution().isBalanced(TreeNode.from_list([1,2,2,3,3,None,None,4,4]))
    False
    >>> Solution().isBalanced(None)
    True
    """
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.recur(root)[0]

    def recur(self, root: Optional[TreeNode]) -> tuple[bool, int]:
        if root is None:
            return (True, 0)
        left_balanced, left_height = self.recur(root.left)
        if not left_balanced:
            return (False, -1)
        right_balanced, right_height = self.recur(root.right)
        if not right_balanced:
            return (False, -1)
        return (abs(left_height - right_height) <= 1, max(left_height, right_height) + 1)
