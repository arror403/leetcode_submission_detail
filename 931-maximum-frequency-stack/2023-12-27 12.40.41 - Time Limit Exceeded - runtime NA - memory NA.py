class FreqStack:

    def __init__(self):
        self.s=[]
        self.d=defaultdict(int)

    def push(self, val: int) -> None:
        self.s.append(val)
        self.d[val]+=1

    def pop(self) -> int:
        t=max(self.d.values())
        r=[k for k,v in self.d.items() if v==t]
        for i in range(len(self.s)-1,-1,-1):
            tmp=self.s[i]
            if tmp in r:
                self.d[tmp]-=1
                del self.s[i]
                return tmp


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()