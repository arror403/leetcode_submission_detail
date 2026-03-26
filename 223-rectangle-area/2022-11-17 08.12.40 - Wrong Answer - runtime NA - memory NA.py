class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        r1=[ax1,ax2,bx1,bx2]
        r1.sort()
        r2=[ay1,ay2,by1,by2]
        r2.sort()

        # print(abs((ax1-ax2)*(ay1-ay2)),abs((bx1-bx2)*(by1-by2)),abs((r1[1]-r1[2])-(r2[1]-r2[2])))

        return abs((ax1-ax2)*(ay1-ay2))+abs((bx1-bx2)*(by1-by2))-abs((r1[1]-r1[2])*(r2[1]-r2[2]))