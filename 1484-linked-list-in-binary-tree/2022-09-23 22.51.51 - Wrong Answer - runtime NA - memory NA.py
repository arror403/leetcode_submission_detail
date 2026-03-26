# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        l=self.LinkedToArr(head)
        r=[]
        
        def allPaths(node):  
            if node:
                if not node.left and not node.right: # Leaf
                    yield [node.val]
                else:
                    yield from ([node.val] + arr for arr in allPaths(node.left))
                    yield from ([node.val] + arr for arr in allPaths(node.right))
                    
        m=list(allPaths(root))
        for i in m: r.append(''.join([str(j) for j in i]))
        l=''.join([str(j) for j in l])
        for i in r:
            if l in r: return True
        return False
    
    def LinkedToArr(self, head):
        arr = []
        curr = head
        while (curr != None): 
            arr.append(curr.val)
            curr = curr.next
        return arr