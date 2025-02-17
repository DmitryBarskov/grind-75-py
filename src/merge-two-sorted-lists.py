from typing import Optional

from list_node import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    >>> list(Solution().mergeTwoLists(ListNode.from_list([1,2,4]), ListNode.from_list([1,3,4])))
    [1, 1, 2, 3, 4, 4]
    >>> Solution().mergeTwoLists(None, None) is None
    True
    >>> list(Solution().mergeTwoLists(None, ListNode.from_list([0])))
    [0]
    """
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val <= list2.val:
            return ListNode(list1.val, self.mergeTwoLists(list1.next, list2))
        return ListNode(list2.val, self.mergeTwoLists(list1, list2.next))
