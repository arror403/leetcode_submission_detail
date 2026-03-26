class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        sum=0
        for i in triangle:
            i.sort()
        for i in triangle:
            sum=sum+i[0]
            
        return sum