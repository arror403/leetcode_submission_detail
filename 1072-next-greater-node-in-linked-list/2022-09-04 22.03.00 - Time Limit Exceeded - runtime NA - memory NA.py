# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        m=self.LinkedToArr(head)
        res=[0]*len(m)
        
        for i in range(len(m)):
            for j in range(i+1,len(m)):
                if m[j]>m[i]:
                    res[i]=m[j]
                    break
        
        
        return res
      
        

        
        
    def LinkedToArr(self, head):
        arr = []
        curr = head
        while (curr != None): 
            arr.append(curr.val)
            curr = curr.next
        return arr