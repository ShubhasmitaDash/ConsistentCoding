# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        List=[]
        count=1
        temp=head
        while temp:
            if left <= count <= right:
                List.append(temp.val)
            count+=1
            temp=temp.next
        List.reverse()
        temp = head
        count = 1
        i = 0

        while temp:
            if left <= count <= right:
                temp.val = List[i]
                i += 1

            temp = temp.next
            count += 1

        return head