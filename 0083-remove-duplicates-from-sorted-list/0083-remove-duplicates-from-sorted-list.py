# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return

        itr = head
        while itr and itr.next:
            if itr.val == itr.next.val:   # duplicate found
                itr.next = itr.next.next  # skip the duplicate node
            else:
                itr = itr.next            # move forward if no duplicate
        return head



        