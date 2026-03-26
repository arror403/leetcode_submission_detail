class Solution:
    def minimumCost(self, source, target, original, changed, cost):
        graph=defaultdict(dict)
        for o,c,w in zip(original,changed,cost):
            if c not in graph[o] or w<graph[o][c]:
                graph[o][c]=w
        
        def dijkstra(start):
            distances={}
            pq=[(0,start)]
            while pq:
                dist,node=heapq.heappop(pq)
                if node in distances: continue

                distances[node]=dist
                
                for neighbor,weight in graph[node].items():
                    if neighbor not in distances:
                        heapq.heappush(pq, (dist+weight,neighbor))

            return distances
        
        
        total_cost=0
        for s,t in zip(source,target):
            if s!=t:
                distances=dijkstra(s)

                if t not in distances: return -1

                total_cost+=distances[t]
        

        return total_cost