class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.q=defaultdict(list)
        for i,v in enumerate(arr):
            self.q[v].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        res=0
        for i in self.q[value]:
            if i>=left and i<=right:
                res+=1
        return res