class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        b=[]
        d=999999999999
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if abs(arr[i]-arr[j])<d:
                    d=abs(arr[i]-arr[j])
     

        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if abs(arr[i]-arr[j])==d:
                    tmp=[arr[i],arr[j]]
                    b.append(tmp)
                    
        return b