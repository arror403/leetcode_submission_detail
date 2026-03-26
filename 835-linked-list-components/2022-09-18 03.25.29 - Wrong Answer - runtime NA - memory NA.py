# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        m=self.LinkedToArr(head)

        
        g=Graph(len(m))
        
        for i in range(1,len(nums)): g.addEdge(nums[i-1],nums[i])
            
        return len(g.connectedComponents())
        
        
    def LinkedToArr(self, head):
        arr = []
        curr = head
        while (curr != None): 
            arr.append(curr.val)
            curr = curr.next
        return arr
    


class Graph:
        # init function to declare class variables
        def __init__(self, V):
            self.V = V
            self.adj = [[] for i in range(V)]

        def DFSUtil(self, temp, v, visited):

            # Mark the current vertex as visited
            visited[v] = True

            # Store the vertex to list
            temp.append(v)

            # Repeat for all vertices adjacent
            # to this vertex v
            for i in self.adj[v]:
                if visited[i] == False:

                    # Update the list
                    temp = self.DFSUtil(temp, i, visited)
            return temp

        # method to add an undirected edge
        def addEdge(self, v, w):
            self.adj[v].append(w)
            self.adj[w].append(v)

        # Method to retrieve connected components
        # in an undirected graph
        def connectedComponents(self):
            visited = []
            cc = []
            for i in range(self.V):
                visited.append(False)
            for v in range(self.V):
                if visited[v] == False:
                    temp = []
                    cc.append(self.DFSUtil(temp, v, visited))
            return cc