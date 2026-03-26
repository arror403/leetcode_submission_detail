class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        def dijkstra(nodes, adjacent, start, end):
            """
            Finds the shortest path from start to end using Dijkstra's algorithm.
            
            Args:
                nodes: Dictionary mapping nodes to their costs
                adjacent: Dictionary mapping nodes to their adjacent nodes
                start: Starting node
                end: Target node
                
            Returns:
                A tuple containing:
                - min_cost: The minimum cost to reach the end node
                - path: The path from start to end as a list of nodes
                - visited_nodes: Total number of nodes visited during algorithm execution
            """
            # Priority queue with (cost, node, path)
            pq = [(0, start, [start])]
            # Keep track of visited nodes and their minimum costs
            visited = {}
            
            while pq:
                cost, node, path = heappop(pq)
                
                # If we've reached the end node, return the cost and path
                if node == end:
                    # return cost, path, len(visited)
                    return cost
                    
                # If we've already found a better path to this node, skip it
                if node in visited and visited[node] <= cost:
                    continue
                    
                visited[node] = cost
                
                # Explore all adjacent nodes
                for next_node in adjacent[node]:
                    # Calculate the cost to visit the next node
                    next_cost = cost + nodes[next_node]
                    
                    if next_node not in visited or next_cost < visited[next_node]:
                        # Add to priority queue with updated cost and path
                        heappush(pq, (next_cost, next_node, path + [next_node]))
            
            # If no path is found, return infinity
            return float('inf'), [], len(visited)

        
        def matrix_to_graph(matrix):
            """
            Convert a m*n matrix to a graph representation.
            
            Args:
                matrix: A 2D list representing the matrix where each cell is either 0 or 1.
                    Nodes with value 1 cost 1 to visit, and nodes with value 0 cost 0 to visit.
            
            Returns:
                A tuple containing:
                - nodes: A dictionary mapping node positions (i, j) to their costs
                - edges: A list of edges as tuples ((i1, j1), (i2, j2))
                - adjacent: A dictionary mapping each node to its adjacent nodes
            """
            if not matrix or not matrix[0]:
                return {}, [], {}
            
            m = len(matrix)
            n = len(matrix[0])
            
            nodes = {}
            edges = []
            adjacent = {(i, j): [] for i in range(m) for j in range(n)}
            
            # Create nodes with their costs
            for i in range(m):
                for j in range(n):
                    # Position (i, j) maps to cost (0 or 1)
                    nodes[(i, j)] = matrix[i][j]
            
            # Create edges between adjacent cells (4-directional: up, down, left, right)
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
            
            for i in range(m):
                for j in range(n):
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        # Check if the adjacent cell is within bounds
                        if 0 <= ni < m and 0 <= nj < n:
                            edges.append(((i, j), (ni, nj)))
                            adjacent[(i, j)].append((ni, nj))
            
            return nodes, edges, adjacent

        
        m = len(grid)
        n = len(grid[0])
        nodes, edges, adjacent = matrix_to_graph(grid)
        start = (0, 0)
        end = (m-1, n-1)


        return dijkstra(nodes, adjacent, start, end)