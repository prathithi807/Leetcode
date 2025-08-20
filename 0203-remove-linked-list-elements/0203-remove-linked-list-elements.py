# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        node = ListNode()       # create a dummy node
        node.next = head        # dummy node points to head
        temp = node             # temp used for traversal

        while (temp.next != None):
            if (temp.next.val == val):           # if next node contains the value
                temp.next = temp.next.next       # skip the node (delete it)
            else:
                temp = temp.next                 # move forward

        return node.next       # return new head
