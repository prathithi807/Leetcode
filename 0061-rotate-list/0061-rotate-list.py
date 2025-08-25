# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # Edge case: empty list or single node
        if not head or not head.next or k == 0:
            return head

        # Step 1: Find the length of the list and the tail
        length, tail = 1, head
        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: Optimize k
        k = k % length
        if k == 0:
            return head

        # Step 3: Find the pivot (new head will be after this node)
        cur = head
        for _ in range(length - k - 1):
            cur = cur.next

        # Step 4: Rotate
        newHead = cur.next
        cur.next = None
        tail.next = head

        return newHead
        