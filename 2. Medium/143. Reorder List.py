# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head1 = head
        head2 = slow.next
        slow.next = None

        prev, nxt = None, None
        while head2:
            nxt = head2.next
            head2.next = prev
            prev = head2
            head2 = nxt
        head2 = prev

        nxt = None
        while head2:
            nxt = head1.next
            head1.next = head2
            head1 = nxt
            nxt = head2.next
            head2.next = head1
            head2 = nxt
