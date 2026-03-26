class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res=[0]*n

        for a,b,s in bookings:
            for i in range(a-1,b):
                res[i]+=s


        return res