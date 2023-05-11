from collections import defaultdict
class Graph:
    # Constructor
    def __init__(self):
        # Initializing Adajency list.
        self.adj=defaultdict(list)
    # Function to insert an edge
    # in the graph.
    def insertEdge(self, u, v):
        # Adding edge from u to v.
        self.adj[u].append(v)
        # Adding edge from v to u.
        self.adj[v].append(u)
    # A helper function for DFS. 
    def DFS_helper(self, u, visited):
        # Marking u as visited
        visited.add(u)
        # Printing its value
        print(u)
        # Checking for all the 
        # node adjacent to u.        
        for v in self.adj[u]:
            # If any adjacent node is 
            # not visited till now.
            if(v not in visited):
                # Then, call DFS_helper with index
                # as v.
                self.DFS_helper(v, visited)
    # DFS function  
    def DFS(self, u):
        # Declaring a visited set.
        visited=set()
        # Calling DFS_helper function 
        # with index as u.
        self.DFS_helper(u,visited)
# Declaring an object 
# of graph type.
g=Graph()        
# Add all the edges through
# insertEdge function.
g.insertEdge(0,1)
g.insertEdge(0,3)
g.insertEdge(1,4)
g.insertEdge(1,2)
g.insertEdge(2,3)
g.insertEdge(4,5)
g.insertEdge(4,6)
g.insertEdge(5,6)
# Call for DFS with 
# index as 0. 
print("The DFS traversal of the given graph starting from node 0 is -")
g.DFS(0)
