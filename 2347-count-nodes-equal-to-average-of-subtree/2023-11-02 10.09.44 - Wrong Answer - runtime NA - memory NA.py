# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        res=0
        for node_value,avg in self.average_subtree_values(root).items():
            if node_value==avg: res+=1

        return res


    def average_subtree(self, node):
        if node is None:
            return (0, 0)  # Return a tuple (sum, count)

        left_sum, left_count = average_subtree(node.left)
        right_sum, right_count = average_subtree(node.right)

        subtree_sum = left_sum + right_sum + node.val
        subtree_count = left_count + right_count + 1

        return (subtree_sum, subtree_count)

    def average_subtree_values(self, root):
        averages = {}  # Dictionary to store average values for each node

        def dfs(node):
            if node is None: return (0,0)

            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            subtree_sum = left_sum + right_sum + node.val
            subtree_count = left_count + right_count + 1

            average = subtree_sum // subtree_count
            averages[node.val] = average

            return (subtree_sum, subtree_count)

        dfs(root)
        return averages