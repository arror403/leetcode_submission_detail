class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        L=len(arr)
        s=set()
        s.add(start)

        def solve(i, v):
            if (i+v)>=L and (i-v)<0: return False

            if (i+v)<L:
                if arr[i+v]==0:
                    return True
                elif (i+v) not in s:
                    s.add((i+v))                    
                    return solve(i+v, arr[i+v])
                else:
                    return False

            if (i-v)>=0:
                if arr[i-v]==0:
                    return True
                elif (i-v) not in s:
                    s.add((i-v))                    
                    return solve(i-v, arr[i-v])
                else:
                    return False


        return solve(start, arr[start])