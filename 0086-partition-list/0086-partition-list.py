# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Dummy heads for two lists
        before_head = ListNode(0)   # List of nodes < x
        after_head = ListNode(0)    # List of nodes >= x

        # Pointers for building the two lists
        before = before_head
        after = after_head

        # Traverse the original list
        while head:
            if head.val < x:
                before.next = head   # attach to before list
                before = before.next
            else:
                after.next = head    # attach to after list
                after = after.next
            head = head.next

        # Connect before list with after list
        after.next = None            # important! avoid cycle
        before.next = after_head.next

        # Return new head
        return before_head.next

        