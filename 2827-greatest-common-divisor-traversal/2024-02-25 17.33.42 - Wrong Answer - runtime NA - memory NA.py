class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        nums = list(set(nums))  # Remove duplicates
        L = len(nums)
        if L <= 1:
            return True

        d = {k: self.prime_factors(k) for k in nums}  # Map each number to its prime factors

        # Create a graph to represent connections based on shared prime factors
        graph = {i: [] for i in range(L)}
        for i in range(L):
            for j in range(i + 1, L):
                if d[nums[i]].intersection(d[nums[j]]):
                    graph[i].append(j)
                    graph[j].append(i)

        # Connection between the first and last elements if they share a prime number
        if d[nums[0]].intersection(d[nums[-1]]):
            graph[0].append(L - 1)
            graph[L - 1].append(0)

        # Use DFS to check connectivity
        visited = set()
        stack = [0]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                stack.extend(graph[node])

        return len(visited) == L

    def prime_factors(self, n):
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