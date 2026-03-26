class Solution:
    def gcdSort(self, nums: List[int]) -> bool:

        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        max_num = max(nums)
        parent = list(range(max_num + 1))

        # Build the Union-Find based on GCD relationships
        for num in nums:
            for multiple in range(num * 2, max_num + 1, num):
                if math.gcd(num, multiple) != 1:
                    parent[find(num)] = find(multiple)

        sorted_nums = sorted(nums)

        for i in range(len(nums)):
            if find(nums[i]) != find(sorted_nums[i]):
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