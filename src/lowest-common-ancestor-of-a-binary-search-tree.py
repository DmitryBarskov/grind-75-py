from tree_node import TreeNode

from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    >>> Solution().lowestCommonAncestor(
    ...     TreeNode.from_list([6,2,8,0,4,7,9,None,None,3,5]),
    ...     TreeNode(2), TreeNode(8)
    ... ).val
    6
    >>> Solution().lowestCommonAncestor(
    ...     TreeNode.from_list([6,2,8,0,4,7,9,None,None,3,5]),
    ...     TreeNode(2), TreeNode(4)
    ... ).val
    2
    >>> Solution().lowestCommonAncestor(
    ...     TreeNode.from_list([2,1]),
    ...     TreeNode(2), TreeNode(1)
    ... ).val
    2
    """

    def lowestCommonAncestor(
            self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'
    ) -> Optional['TreeNode']:
        return self.recur(root, p, q)[0]

    def recur(
            self, root: Optional['TreeNode'], p: 'TreeNode', q: 'TreeNode'
    ) -> tuple[Optional['TreeNode'], int]:
        """
        returns (common root if count_of_found_nodes == 2 else None, count_of_found_nodes)
        """
        if root is None:
            return (None, 0)

        found_in_self = 1 if root.val in (p.val, q.val) else 0
        candidate, found_in_left = self.recur(root.left, p, q)
        if found_in_left == 2:
            return (candidate, 2)
        candidate, found_in_right = self.recur(root.right, p, q)
        if found_in_right == 2:
            return (candidate, 2)
        if found_in_self + found_in_left + found_in_right >= 2:
            return (root, 2)
        return (None, found_in_self + found_in_left + found_in_right)
