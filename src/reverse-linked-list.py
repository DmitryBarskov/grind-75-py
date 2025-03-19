from typing import Optional

from list_node import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    >>> Solution().reverseList(ListNode.from_list([1,2,3,4,5])).to_list()
    [5, 4, 3, 2, 1]
    >>> Solution().reverseList(ListNode.from_list([1,2])).to_list()
    [2, 1]
    >>> Solution().reverseList(ListNode.from_list([])) is None
    True
    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed_head: Optional[ListNode] = None
        it: Optional[ListNode] = head
        while it is not None:
            reversed_head = ListNode(it.val, reversed_head)
            it = it.next
        return reversed_head
