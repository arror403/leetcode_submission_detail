class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        def prime_factors(n):
            factors = set()
            while n % 2 == 0:
                factors.add(2)
                n //= 2
            for i in range(3, int(n**0.5) + 1, 2):
                while n % i == 0:
                    factors.add(i)
                    n //= i
            if n > 2:
                factors.add(n)
            return factors

        # Create a dictionary to store neighbors with shared prime factors
        prime_neighbors = {}

        # Populate prime_neighbors
        for i in range(len(nums)):
            factors_i = prime_factors(nums[i])
            for j in range(i + 1, len(nums)):
                factors_j = prime_factors(nums[j])
                if factors_i.intersection(factors_j):
                    if i not in prime_neighbors:
                        prime_neighbors[i] = set()
                    if j not in prime_neighbors:
                        prime_neighbors[j] = set()
                    prime_neighbors[i].add(j)
                    prime_neighbors[j].add(i)

        # Depth First Search to check connectivity
        visited = set()
        stack = []

        # Start DFS from any node
        start_node = 0
        stack.append(start_node)

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                stack.extend(prime_neighbors.get(node, []))

        # If all nodes are visited, then the graph is connected
        return len(visited) == len(nums)