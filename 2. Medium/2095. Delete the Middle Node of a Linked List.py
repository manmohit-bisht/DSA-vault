# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        slow, fast = head, head
        if head is None or head.next is None:
            return None

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if slow.next is None:
            head.next = None
            return head
        else:
            slow.val = slow.next.val
            slow.next = slow.next.next
            return head
