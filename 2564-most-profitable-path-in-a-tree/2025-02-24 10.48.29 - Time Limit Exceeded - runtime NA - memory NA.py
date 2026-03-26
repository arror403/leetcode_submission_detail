class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n=len(amount)
        adj=[[] for _ in range(n)]

        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])

        disFromBob=[0]*n

        @lru_cache(None)
        def dfs(u, par, depth, amount):
            ret = 0
            disFromBob[u] = 0 if u==bob else len(amount)

            maxChild = -inf
            for v in adj[u]:
                if v==par: continue
                maxChild = max(maxChild, dfs(v, u, depth+1, amount))
                disFromBob[u] = min(disFromBob[u], disFromBob[v]+1)

            if(disFromBob[u]>depth):
                ret+=amount[u]
            elif(disFromBob[u]==depth):
                ret+=amount[u]//2

            if(maxChild==-inf):
                return ret
            else:
                return ret+maxChild


        return dfs(0,0,0,tuple(amount))