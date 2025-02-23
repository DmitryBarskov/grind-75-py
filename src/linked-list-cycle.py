from typing import Optional

from list_node import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    >>> head = ListNode(3)
    >>> head.next = ListNode(2)
    >>> head.next.next = ListNode(0)
    >>> head.next.next.next = ListNode(4)
    >>> head.next.next.next.next = head.next
    >>> Solution().hasCycle(head)
    True
    >>> head = ListNode(1)
    >>> head.next = ListNode(2)
    >>> head.next.next = head
    >>> Solution().hasCycle(head)
    True
    >>> Solution().hasCycle(ListNode(1))
    False
    """
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
