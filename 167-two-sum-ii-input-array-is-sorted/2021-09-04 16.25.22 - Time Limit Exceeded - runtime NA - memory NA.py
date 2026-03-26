class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        tmp = 0
        b=[]
        for i in range(len(numbers)):
            if (numbers[i] <= target):
                tmp+=numbers[i]
                for j in range(i,len(numbers)):
                    if tmp+numbers[j] == target and i != j:
                        b.append(i+1)
                        b.append(j+1)
                        break
            tmp=0
                        
        return b
                    