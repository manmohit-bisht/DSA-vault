# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        head = None
        curr = None
        carry = 0
        while l1 or l2 or carry:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            total = a + b + carry
            carry = (
                1 if total >= 10 else 0
            )  # or total//10,both works but here since we only have 1 digit, carry can only be 0 or 1
            newNode = ListNode(total % 10)

            if head is None:
                head = newNode
                curr = head
            else:
                curr.next = newNode
                curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return head
