class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        a=sum(distance[start:destination])
        b=sum(distance)-a
        # print 
        return a if a<=b else b
