class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        s=sum(apple)
        res=0
        for i in sorted(capacity,reverse=True):
            if s-i>=0:
                res+=1
                s-=i
        return res