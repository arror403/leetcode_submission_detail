class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        
        # Initialize a Union-Find data structure
        def initialize_union_find(nums):
            parent = {}
            for num in nums:
                parent[num] = num
            return parent

        # Find operation in Union-Find
        def find(num):
            if parent[num] == num:
                return num
            parent[num] = find(parent[num])
            return parent[num]

        # Union operation in Union-Find
        def union(a, b):
            root_a = find(a)
            root_b = find(b)
            if root_a != root_b:
                parent[root_a] = root_b

        parent = initialize_union_find(range(1, max(nums) + 1))

        # Build the Union-Find based on GCD relationships
        for num in nums:
            for divisor in range(2, int(num ** 0.5) + 1):
                if num % divisor == 0:
                    union(num, divisor)
                    union(num, num // divisor)

        # Check if the original order and sorted order have the same connected components
        for i in range(len(nums)):
            if find(nums[i]) != find(sorted(nums)[i]):
                return False

        return True



        # def find_coprime(numbers):
        #     res=[]
        #     for i,num in enumerate(numbers):
        #         # Check if the current number is coprime to all other numbers.
        #         if all((math.gcd(num, other)==1) for other in numbers if other != num):
        #             res.append(i)
        #     return res

        # p=find_coprime(nums)

        # nums.sort()

        # q=find_coprime(nums)

        # return p==q