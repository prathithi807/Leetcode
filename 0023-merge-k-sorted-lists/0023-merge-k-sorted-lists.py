# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        tmp1, tmp2, tmp3 = list1, list2, head

        while tmp1 is not None and tmp2 is not None:
            if tmp1.val <= tmp2.val:
                tmp3.next = tmp1
                tmp1 = tmp1.next
            else:
                tmp3.next = tmp2
                tmp2 = tmp2.next
            tmp3 = tmp3.next

        if tmp1 is not None:
            tmp3.next = tmp1

        if tmp2 is not None:
            tmp3.next = tmp2

        return head.next   # return merged list (skip dummy node)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        # Keep merging lists two at a time until only one list remains
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                merged.append(self.mergeTwoLists(l1, l2))
            lists = merged  # replace with newly merged lists

        return lists[0]

        