class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0]*size for _ in range(size)]
        self.size = size

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight  # For undirected graph

    def dijkstra(self, start_vertex, end_vertex):
        distances = [inf] * self.size
        distances[start_vertex] = 0
        visited = [False] * self.size

        for _ in range(self.size):
            min_distance = inf
            u = None
            for i in range(self.size):
                if not visited[i] and distances[i] < min_distance:
                    min_distance = distances[i]
                    u = i
            
            if u is None or u == end_vertex:
                break
            
            visited[u] = True
            for v in range(self.size):
                if self.adj_matrix[u][v] != 0 and not visited[v]:
                    alt = distances[u] + self.adj_matrix[u][v]
                    if alt < distances[v]:
                        distances[v] = alt

        return distances[end_vertex]


class Solution:
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        g = Graph(n)
        for (u, v), p in zip(edges, succProb):
            g.add_edge(u, v, -log10(p))  # Use negative log for maximizing probability
        
        shortest_path = g.dijkstra(start_node, end_node)
        return 10 ** (-shortest_path) if shortest_path != inf else 0