# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:


        def inorder_with_parentheses(root):
            if root.left is None and root.right is None:
                return str(root.val)

            result = ""
            if root.left is not None:
                result += "(" + inorder_with_parentheses(root.left)

            result += str(root.val)

            if root.right is not None:
                result += inorder_with_parentheses(root.right) + ")"

            return result


        t=inorder_with_parentheses(root)
        res=''
        m="01|&"

        for i in t:
            if i in '0123':
                res+=m[int(i)]
            else:
                res+=i

        return eval(res)