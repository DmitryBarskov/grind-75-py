from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    # pylint: disable-next=redefined-builtin
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def from_list(l: List[int]) -> Optional['ListNode']:
        list_node = None
        for item in reversed(l):
            list_node = ListNode(item, list_node)
        return list_node

    def to_list(self):
        return list(self)

    def __iter__(self):
        return ListNode.Iterator(self)

    class Iterator:
        def __init__(self, rest: Optional['ListNode']):
            self.rest = rest

        def __next__(self) -> int:
            if self.rest is None:
                raise StopIteration
            item = self.rest.val
            self.rest = self.rest.next
            return item

        def __iter__(self):
            return self
