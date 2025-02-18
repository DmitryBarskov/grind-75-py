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
    >>> Solution().invertTree(TreeNode.from_list([4, 2, 7, 1, 3, 6, 9])).to_list()
    [4, 7, 2, 9, 6, 3, 1]
    >>> Solution().invertTree(TreeNode.from_list([2, 1, 3])).to_list()
    [2, 3, 1]
    >>> Solution().invertTree(None) is None
    True
    """
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        return TreeNode(
                root.val,
                self.invertTree(root.right),
                self.invertTree(root.left)
        )
