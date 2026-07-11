# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        temp=head
        count=0
        while temp:
            temp=temp.next
            count+=1
        dummy=ListNode(0)
        dummy.next=head
        group_prev=dummy
        for i in range(count//k):
            group_start=group_prev.next
            curr=group_start
            prev=None
            for i in range(k):
                new=curr.next
                curr.next=prev
                prev=curr
                curr=new
            group_prev.next=prev
            group_start.next=curr
            group_prev=group_start
        return dummy.next