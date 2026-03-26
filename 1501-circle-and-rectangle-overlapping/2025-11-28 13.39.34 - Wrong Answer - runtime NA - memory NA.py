class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:

        l = sqrt(((x2-x1)/2)**2 + ((y2-y1)/2)**2)

        return dist(((x2+x1)/2, (y2+y1)/2), (xCenter, yCenter)) <= l+radius