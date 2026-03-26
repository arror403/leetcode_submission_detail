class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]

        def get_all_partition(m, index, ans):
            nonlocal res

            if index==len(m):
                tmp=[''.join(j for j in i) for i in ans]
                # print(tmp)
                if any(r!=r[::-1] for r in tmp):
                    return
                else:
                    res.append(tmp)
                    return
                
            # For each subset in the partition, add the current element to it and recall
            for i in range(len(ans)):
                ans[i].append(m[index])
                get_all_partition(m, index+1, ans)
                ans[i].pop()
        
            # Add the current element as a singleton subset and recall
            ans.append([m[index]])
            get_all_partition(m, index+1, ans)
            ans.pop()


        get_all_partition(s,0,[])


        return res