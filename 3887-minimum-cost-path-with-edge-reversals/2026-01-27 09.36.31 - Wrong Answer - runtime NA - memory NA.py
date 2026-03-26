class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        # Function to do DFS through the nodes
        def minimumCostSimplePath(u, destination, visited, graph):
            # Check if we find the destination then further cost will be 0
            if u == destination: return 0
            # Marking the current node as visited
            visited[u] = 1
            ans = inf
            # Traverse through all the adjacent nodes
            for i in range(n):
                if (graph[u][i] != inf and not visited[i]):
                    # Cost of the further path
                    cur = minimumCostSimplePath(i, destination, visited, graph)
                    # Check if we have reached the destination
                    if (cur < inf):
                        # Taking the minimum cost path
                        ans = min(ans, graph[u][i] + cur)
            # Unmarking the current node to make it available for other simple paths
            visited[u] = 0

            return ans

        graph = [[inf]*n for _ in range(n)]
        for u, v, w in edges:
            graph[u][v] = w
            graph[v][u] = w*2

        visited = [0]*n

        res = minimumCostSimplePath(0, n-1, visited, graph)
        return -1 if res==inf else res