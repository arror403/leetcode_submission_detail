# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.inorderTraversal(p)==self.inorderTraversal(q) and self.PreorderTraversal(p)==self.PreorderTraversal(q)
        
        
        
        
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.val)
            res += self.inorderTraversal(root.right)
        return res
    
    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.val)
            res += self.PreorderTraversal(root.left)
            res += self.PreorderTraversal(root.right)
        return res