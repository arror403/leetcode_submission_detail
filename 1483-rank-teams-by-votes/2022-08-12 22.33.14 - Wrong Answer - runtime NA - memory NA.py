class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        res=''
        d=dict.fromkeys(string.ascii_uppercase, 0)
        for i in votes:
            for j in range(len(i)):
                d[i[j]]+=(j+1)
                
        d=dict(sorted(d.items(), key=lambda item: item[1]))
        print(d)
        
        for i in d:
            if d[i]!=0:
                res+=i
        return res