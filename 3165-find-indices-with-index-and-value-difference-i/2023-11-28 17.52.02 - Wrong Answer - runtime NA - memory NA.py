class Solution:
    def findIndices(self, nums: List[int], Di: int, Dv: int) -> List[int]:
        t=[[i[0],j[0]] for i,j in combinations([[i,v] for i,v in enumerate(nums)],2) if (abs(i[0]-j[0])>=Di and abs(i[1]-j[1])>=Dv)]
        return t[0] if t else [-1,-1]