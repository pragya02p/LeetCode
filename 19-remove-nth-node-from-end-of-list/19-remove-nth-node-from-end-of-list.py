# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next==None and n==1:
            return None
        h=head
        c=1
        while  h.next!= None:
            h=h.next
            c+=1
        if c-n==0:
            head=head.next
            return head
        p=head
        nxt=head
        for i in range(c-n-1):
            p=p.next
            nxt=nxt.next
        if p.next!=None:
            p.next=nxt.next.next

        return head
            
            
        