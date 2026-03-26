# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:


        def is_pseudo_palindromic(l):
            odd_count = sum(c%2!=0 for c in Counter(l).values())
            return odd_count<=1


        def allPaths(node):
            if node:
                if not node.left and not node.right:
                    yield [node.val]
                else:
                    yield from ([node.val] + arr for arr in allPaths(node.left))
                    yield from ([node.val] + arr for arr in allPaths(node.right))

        p=allPaths(root)

        return len([i for i in p if is_pseudo_palindromic(i)])