# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # Create two dummy nodes for two lists
        left, right = ListNode(), ListNode()
        
        # These pointers will move as we build the two lists
        ltail, rtail = left, right

        while head:
            if head.val < x:
                ltail.next = head
                ltail = ltail.next
            else:
                rtail.next = head
                rtail = rtail.next
            head = head.next

        # Connect the two lists
        ltail.next = right.next
        # Important: cut off the tail of right list
        rtail.next = None  

        return left.next


        