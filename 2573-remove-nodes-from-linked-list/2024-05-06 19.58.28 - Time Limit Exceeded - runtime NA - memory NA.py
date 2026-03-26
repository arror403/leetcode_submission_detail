# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # arr=sorted([[i,v] for i,v in enumerate(self.LinkedToArr(head))],key=lambda x:x[1])
        arr=self.LinkedToArr(head)
        L=len(arr)
        res=[]

        for i in range(L):
            for j in range(i+1,L):
                f=True
                if arr[j]>arr[i]:
                    f=False
                    break
                    
            if f: res.append(arr[i])

        if arr[-1]>arr[-2]: res.append(arr[-1])

        return self.ArrToLinked(res)


    def ArrToLinked(self, l):
        cur = dummy = ListNode(0)
        for n in l:
            cur.next = ListNode(n)
            cur = cur.next
        return dummy.next
        
        
    def LinkedToArr(self, head):
        res=[]
        while head: 
            res.append(head.val)
            head=head.next
        return res