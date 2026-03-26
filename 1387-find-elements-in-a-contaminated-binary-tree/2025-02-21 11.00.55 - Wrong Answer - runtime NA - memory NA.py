class FindElements:

    def __init__(self, root: TreeNode):

        def bfs(root: TreeNode) -> None:
            dq = deque([root])
            while dq:
                node = dq.popleft()
                if node.left:
                    node.left.val = 2 * node.val + 1
                    dq.append(node.left)
                    self.seen.add(node.left.val)
                if node.right:
                    node.right.val = 2 * node.val + 2
                    dq.append(node.right)
                    self.seen.add(node.right.val)
            
        self.seen = set()
        if root:
            root.val = 0
            bfs(root)
        

    def find(self, target: int) -> bool:
        return target in self.seen    