class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for i in range(int(math.sqrt(area)),area+1):
            if area%i==0:
                return [i,int(area/i)]