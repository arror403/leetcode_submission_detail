class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Build the graph and calculate in-degrees
        graph = defaultdict(list)
        in_degree = [0] * n
        for from_node, to_node in edges:
            graph[from_node].append(to_node)
            in_degree[to_node] += 1

        # Initialize the result list
        paths = [[] for _ in range(n)]

        # Find nodes with in-degree 0
        queue = [node for node in range(n) if in_degree[node] == 0]

        while queue:
            node = queue.pop(0)
            
            # Update paths of children
            for child in graph[node]:
                if not paths[child]:
                    paths[child] = paths[node] + [node]
                else:
                    paths[child] = (paths[child] + paths[node] + [node])
                
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    queue.append(child)

        return list(map(lambda x: sorted(set(x)), paths))