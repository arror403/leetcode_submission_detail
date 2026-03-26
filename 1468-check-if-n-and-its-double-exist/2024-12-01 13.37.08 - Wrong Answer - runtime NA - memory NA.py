class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        r=set(arr)&set([2*i for i in arr])
        return bool(r) and r!={0}