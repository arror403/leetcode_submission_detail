class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        return all([r==r[:k]+r[k:] if i%2!=0 else r==r[k:]+r[:k] for i,r in enumerate(mat)])
