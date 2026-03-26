class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0]*size for _ in range(size)]
        self.size = size
        self.vertex_data = [i for i in range(size)]

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight  # For undirected graph

    def dijkstra(self, start_vertex):
        distances = [0] * self.size
        distances[start_vertex] = 1
        visited = [False] * self.size

        for _ in range(self.size):
            max_prob = 0
            u = None
            for i in range(self.size):
                if not visited[i] and distances[i] > max_prob:
                    max_prob = distances[i]
                    u = i
            if u is None:
                break
            visited[u] = True
            for v in range(self.size):
                if self.adj_matrix[u][v] != 0 and not visited[v]:
                    new_prob = distances[u] * self.adj_matrix[u][v]
                    if new_prob > distances[v]:
                        distances[v] = new_prob
        return distances


class Solution:
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        g=Graph(n)
        for (u,v), p in zip(edges,succProb):
            g.add_edge(u,v,p)
        
        probabilities=g.dijkstra(start_node)

        
        return probabilities[end_node]