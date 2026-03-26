# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def allPaths(node):
            if node:
                if not node.left and not node.right: # Leaf
                    yield [node.val]
                else:
                    yield from ([node.val] + arr for arr in allPaths(node.left))
                    yield from ([node.val] + arr for arr in allPaths(node.right))
        m=allPaths(root)
        res=inf
        r=''
        for i in m:
            x=[str(x) for x in i]
            x.reverse()
            tmp=int(''.join(x))
            if tmp<res: res=tmp
        res=list(map(int,str(res)))
        for i in res: r+=chr(i+97)
            
        return r