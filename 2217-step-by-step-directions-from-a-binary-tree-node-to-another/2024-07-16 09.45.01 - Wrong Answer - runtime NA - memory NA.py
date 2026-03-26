# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        p1,p2=[],[]
        self.findPath(root, p1, startValue)
        self.findPath(root, p2, destValue)

        # Find the common ancestor
        i=0
        while i<len(p1) and i<len(p2) and p1[i]==p2[i]: i+=1
        
        # Steps to move up from startValue to the common ancestor
        steps_up_str='U'*(len(p1)-i)
        
        # Steps to move down from the common ancestor to destValue
        steps_down=''.join(['L' if p2[j]==root.left.val else 'R' for j in range(i,len(p2))])
        

        return steps_up_str+steps_down


    def findPath(self, root, path, k):
        if root is None: return False
    
        path.append(root.val)
    
        if root.val==k: return True
    
        # Check if k is found in left or right sub-tree
        if ((root.left and self.findPath(root.left, path, k)) or
            (root.right and self.findPath(root.right, path, k))):
            return True
    
        # If not present in subtree rooted with root, remove
        # root from path and return False
        path.pop()

        return False