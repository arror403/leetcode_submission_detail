class SeatManager:

    def __init__(self, n: int):
        self.s={i:True for i in range(1,n+1)}

    def reserve(self) -> int:
        for k,v in self.s.items():
            if v: 
                self.s[k]=False
                return k

    def unreserve(self, seatNumber: int) -> None:
        self.s[seatNumber]=True
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)