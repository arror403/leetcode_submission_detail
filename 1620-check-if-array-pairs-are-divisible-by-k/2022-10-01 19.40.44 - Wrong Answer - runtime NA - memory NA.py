class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        return sum(arr)%k==0