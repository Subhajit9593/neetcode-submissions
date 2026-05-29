# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        a=list1
        b=list2
        res=ListNode()
        c=res
        while a and b:
            if a.val>=b.val:
                c.next=b
                c=c.next
                b=b.next
            else:
                c.next=a
                c=c.next
                a=a.next
        c.next=a or b
        return res.next




        

        