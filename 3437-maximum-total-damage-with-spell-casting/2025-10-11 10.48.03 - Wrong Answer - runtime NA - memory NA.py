class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        frequencyMap = defaultdict(int)
        for p in power: frequencyMap[p]+=1
        uniquePowers = list(frequencyMap.keys())
        dp = [-1]*len(frequencyMap)

        def getMaxDamage(index):
            if index==len(uniquePowers): return 0
            if dp[index]!=-1: return dp[index]
            # Option 1: Skip the current element
            skip = getMaxDamage(index+1)
            # Option 2: Take the current element
            take = 0
            nextIndex = index+1
            while nextIndex<len(uniquePowers) and (uniquePowers[nextIndex]-uniquePowers[index])<=2:
                nextIndex+=1
            take = frequencyMap[uniquePowers[index]]*uniquePowers[index] + getMaxDamage(nextIndex)
            dp[index] = max(take, skip)
            return dp[index]


        return getMaxDamage(0)



        # d=Counter(power)
        # s={}

        # for v,f in d.items():
        #     s[v]=v*f

        # s=sorted(s.items(), key=lambda x:x[1], reverse=True)
        
        # not_able=set()
        # for a,b in s: