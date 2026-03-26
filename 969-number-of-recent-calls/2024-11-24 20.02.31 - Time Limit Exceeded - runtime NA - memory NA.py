class RecentCounter:

    def __init__(self):
        self.r=[]
        self.d=set()

    def ping(self, t: int) -> int:
        self.r=[t-3000,t]
        self.d.add(t)
        return sum(1 for e in self.d if e>=self.r[0] and e<=self.r[1])



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)