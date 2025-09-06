# Definition for singly-linked list.
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
      dummy=ListNode(0,head)
      prev=dummy
      curr=head
      while curr:
        if curr.next and curr.val==curr.next.val:
          while curr.next and curr.val==curr.next.val:
            curr=curr.next
          prev.next=curr.next
        else:
          prev=prev.next
        curr=curr.next
      return dummy.next






        


        