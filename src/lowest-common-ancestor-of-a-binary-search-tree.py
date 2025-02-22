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
    ) -> 'TreeNode':
        if p.val == q.val:
            return p
        if p.val > q.val:
            return self.lowestCommonAncestor(root, q, p)
        if p.val <= root.val <= q.val:
            return root
        if q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return self.lowestCommonAncestor(root.right, p, q)
