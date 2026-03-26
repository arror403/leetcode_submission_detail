# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # A recursive function to construct a full binary tree from the given preorder
        # and postorder sequence
        def buildTree(preorder, pIndex, start, end, d):
        
            # Consider the next item from the given preorder sequence.
            # This item would be the root node of the subtree formed by
            # the `postorder[start, end]` and increment `pIndex`
            root = TreeNode(preorder[pIndex])
            pIndex = pIndex + 1
        
            # return if all keys are processed
            if pIndex == len(preorder):
                return root, pIndex
        
            # find the next key index in the postorder sequence to determine the
            # boundary of the left and right subtree of the current root node
            index = d.get(preorder[pIndex])
        
            # fill the left and right subtree together
            if start <= index and index + 1 <= end - 1:
                # build the left subtree
                root.left, pIndex = buildTree(preorder, pIndex, start, index, d)
        
                # build the right subtree
                root.right, pIndex = buildTree(preorder, pIndex, index + 1, end - 1, d)
        
            return root, pIndex
        
        
        # Construct a full binary tree from preorder and postorder sequence
        def buildBinaryTree(preorder, postorder):
        
            # base case
            if not preorder:
                return
        
            # dictionary is used to efficiently find the index of any element in the given
            # postorder sequence
            d = {}
            for i, e in enumerate(postorder):
                d[e] = i
        
            # `pIndex` stores the index of the next node in the preorder sequence
            pIndex = 0
        
            # set range [start, end] for subtree formed by postorder sequence
            start = 0
            end = len(preorder) - 1
        
            # construct the binary tree and return it
            return buildTree(preorder, pIndex, start, end, d)[0]
        return buildBinaryTree(preorder,postorder)

