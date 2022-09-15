# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c=0
        head=[]
        node=ListNode()
        while l1!=None or l2!=None:
            
            if l1 and l2:
                v=l1.val+l2.val+c
                if v<=9:
                    head.append(v)
                    
                    c=0
                elif v==10:
                    head.append(0)
                    c=1
                else:
                    head.append(v%10)
                    c=1
                l1=l1.next
                l2=l2.next
            elif l1:
                v=l1.val+c
                if v<=9:
                    head.append(v)
                    c=0
                elif v==10:
                    head.append(0)
                    c=1
                else:
                    head.append(v%10)
                    c=1
                l1=l1.next
            elif l2:
                v=l2.val+c
                if v<=9:
                    head.append(v)
                    c=0
                elif v==10:
                    head.append(0)
                    c=1
                else:
                    head.append(v%10)
                    c=1
                l2=l2.next
        if c!=0:
            head.append(c)
        dummyhead=ListNode(0)
        curr=dummyhead
        for i in head:
            newnode=ListNode(i)
            curr.next=newnode
            curr=newnode
        return dummyhead.next
        
        