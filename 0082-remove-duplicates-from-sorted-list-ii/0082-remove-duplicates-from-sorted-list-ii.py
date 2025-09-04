# Definition for singly-linked list.
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)  # dummy node to handle head deletions easily
        prev = dummy
        curr = head

        while curr:
            # Check if current node is the start of duplicates
            if curr.next and curr.val == curr.next.val:
                # Skip all nodes with this value
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                prev.next = curr.next  # unlink all duplicates
            else:
                prev = prev.next  # move prev if no duplicate
            curr = curr.next

        return dummy.next




        