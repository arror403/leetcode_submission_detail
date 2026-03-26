class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        n = len(x)
        
        # Group indices by their x values
        x_to_indices = defaultdict(list)
        for i in range(n):
            x_to_indices[x[i]].append(i)
        
        # Get all unique x values
        unique_x = list(x_to_indices.keys())
        
        # Need at least 3 distinct x values
        if len(unique_x) < 3:
            return -1
        
        max_sum = -1
        
        # Try all combinations of 3 distinct x values
        for i in range(len(unique_x)):
            for j in range(i + 1, len(unique_x)):
                for k in range(j + 1, len(unique_x)):
                    x1, x2, x3 = unique_x[i], unique_x[j], unique_x[k]
                    
                    # For each distinct x value, find the index with maximum y
                    max_y1 = max(y[idx] for idx in x_to_indices[x1])
                    max_y2 = max(y[idx] for idx in x_to_indices[x2])
                    max_y3 = max(y[idx] for idx in x_to_indices[x3])
                    
                    current_sum = max_y1 + max_y2 + max_y3
                    max_sum = max(max_sum, current_sum)
        
        return max_sum


        
        # dx=defaultdict(list)
        # dy=defaultdict(list)
        # res=0

        # for i in range(len(x)):
        #     dx[x[i]].append(i)
        #     dy[y[i]].append(i)
        
        # if len(dx.keys())<3: return -1

        # dy=dict(sorted(dy.items(), reverse=True))
        # cnt=0
        # seen=set()

        # print(dx,dy)

        # for k,l in dy.items():
        #     if cnt==3: return res

        #     if not set(l)&seen:
        #         res+=k
        #         seen|=set(l)
        #         # for i in l: seen|=set(dx[x[i]])
        #         cnt+=1
 
        #     print(seen,k)


        # return -1