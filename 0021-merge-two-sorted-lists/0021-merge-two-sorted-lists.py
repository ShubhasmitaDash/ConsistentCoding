# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0)
        tail=dummy
        t1=list1
        t2=list2
        while t1 and t2:
            if t1.val<=t2.val:
                tail.next=t1
                tail=tail.next
                t1=t1.next
            else:
                tail.next=t2
                tail=tail.next
                t2=t2.next
        if t1:
            tail.next=t1
        if t2:
            tail.next=t2
        return dummy.next