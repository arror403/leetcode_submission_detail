class Solution:
    def processQueries(self, c, connections, queries) -> List[int]:
        # Step 1: Build the adjacency list representation of the graph.
        adj = defaultdict(list)
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)

        # Step 2: Find all connected components using Depth First Search (DFS).
        ids = {}  
        components = defaultdict(list)
        visited = [False] * (c + 1) # 1 indexed, visited[0] won't be used
        def dfs(node, component_id):
            visited[node] = True
            ids[node] = component_id
            components[component_id].append(node)
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor, component_id)

        # Iterate through all nodes to find all components.
        for i in range(1, c + 1):
            if not visited[i]:
                # We found a new, unvisited component.
                # Use the first node `i` we find as the ID for this component.
                dfs(i, i)
                # Sort the nodes in the component to easily find the smallest later.
                components[i].sort()
        
        # Step 3: Process the queries.
        removed = set()
        res = []
        for q, node in queries:
            if q == 1:  # This is a "find" query.
                # First, check if the queried node itself is available.
                if node not in removed:
                    res.append(node)
                else:
                    # The node was removed. We need to find the smallest available
                    # node in the SAME connected component.
                    component_id = ids.get(node)
                    found_alternative = False
                    # `components[component_id]` list is sorted
                    for candidate_node in components[component_id]:
                        if candidate_node not in removed:
                            res.append(candidate_node)
                            found_alternative = True
                            break
                    if not found_alternative:
                        res.append(-1)
            
            else:
                removed.add(node)
        # print(adj, components, removed)
        
        return res



        # stat = defaultdict(int)
        # s = chain.from_iterable(connections)
        # sorted_s = sorted(s)
        # res = []

        # for q in queries:
        #     if q[0]==1:
        #         if stat[q[1]]==0:
        #             res.append(q[1])
        #         else:
        #             f=1
        #             for x in sorted_s:
        #                 if stat[x]==0:
        #                     f=0
        #                     res.append(x)
        #                     break
        #             if f: res.append(-1)
        #     else:
        #         stat[q[1]]=1


        # return res