class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # m=[]
        # for i,v in enumerate(arr):
        #     m.append([i,v])

        # print(sorted(m, key=lambda x:x[1], reverse=1))


        # return [0]
        # m=max(arr)
        # res=[m]
        return [max(arr[i:]) for i in range(1,len(arr))]+[-1]