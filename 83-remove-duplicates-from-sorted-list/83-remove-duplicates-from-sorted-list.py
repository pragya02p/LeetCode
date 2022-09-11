# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=ListNode()
        prev=head
        if head==None or head.next==None:
            return head
        current=head.next
        while current!=None:
            if prev.val==current.val:
                prev.next=current.next
                current=current.next
            else:
                prev=prev.next
                current=current.next
        return head
        