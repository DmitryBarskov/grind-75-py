from typing import Optional
from tree_node import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    >>> null = None
    >>> Solution().lowestCommonAncestor(
    ...     TreeNode.from_list([3,5,1,6,2,0,8,null,null,7,4]),
    ...     TreeNode(5), TreeNode(1)
    ... ).val
    3
    >>> Solution().lowestCommonAncestor(
    ...     TreeNode.from_list([3,5,1,6,2,0,8,null,null,7,4]),
    ...     TreeNode(5), TreeNode(4)
    ... ).val
    5
    >>> Solution().lowestCommonAncestor(
    ...     TreeNode.from_list([1,2]),
    ...     TreeNode(1), TreeNode(2)
    ... ).val
    1
    """
    def lowestCommonAncestor(
            self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'
    ) -> 'TreeNode':
        lca, _ = self.__recur(root, p, q)
        if lca is None:
            raise TypeError
        return lca

    def __recur(
            self, root: Optional['TreeNode'], p: 'TreeNode', q: 'TreeNode'
    ) -> tuple[Optional['TreeNode'], int]:
        if root is None:
            return (None, 0)
        lca, found_in_left = self.__recur(root.left, p, q)
        if lca is not None:
            return (lca, 2)
        lca, found_in_right = self.__recur(root.right, p, q)
        if lca is not None:
            return (lca, 2)
        found_in_self = 1 if root.val in (p.val, q.val) else 0
        total_found = found_in_self + found_in_left + found_in_right
        if total_found >= 2:
            return (root, total_found)
        return (None, total_found)
