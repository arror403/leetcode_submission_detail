class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.q=arr

    def query(self, left: int, right: int, value: int) -> int:
        return Counter(self.q[left:right+1])[value]


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)