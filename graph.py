# ALL THE GRAPH ALGO 

# queue implementation 
import queue


class Queue:
    def ___init__(self):
        self.queue=[]
    def addq(self, v):
        self.queue.append(v)
    def delq(self):
        v=None
        if not self.isempty():
            v=self.queue[0]
            self.queue=self.queue[1:]
            return(v)
    def isempty(self):
        return (self.queue==[])
    def __str__(self):
        return(str(self.queue))

# making graph if edges joints are given 
nodes=5 
edges=[(0,1),(0,4),(1,2),(2,3),(1,3),(1,4),(3,4)] 

# there are two ways of representing a graph 
# first is adjacency list and second is adjacency matrix

# adjacency list 
#using oops 
class Graph:
    def __init__(self, num_nodes, edges):
        self.num_nodes= num_nodes
        self.edges= edges 
        self.data=[[] for _ in range (num_nodes)]
        # gives a list of list in range no of nodes 
        for i, j in  edges:
            self.data[i].append(j)
            self.data[j].append(i)
            #now we get 2d list where the index of list point to the nodes of graph and the data in list point to the nodes it is connnected to 

        #enumerate gives us value with index
    def __repr__(self):
        #making strings
        return "\n".join(["{}:{}".format(n, neighbours) for n, neighbours in enumerate(self.data)])
        # by doing enumerate self..data we get the data with index i.e vertices it is connected to 
        # n points to vertex and neighbours point to list of vertices it is connected to 
        # and hence it is appended in a list joined by "\n"
    def __str__(self):
        return self.__repr__()
    def addedge (self, neweddge):
        for i, j in newedge:
            self.data[i].append(j)
            self.data[j].append(i)
    def remedge (self, remedge):
        for i, j in remedge:
            self.data[i].remove(j)
            self.data[j].remove(i)
    def dfs(graph, root):
        stack=[]
        result=[]
        discovered=[False]*graph.num_nodes
        stack.append(root)

        while (len(stack)>0):
            current=stack.pop()
            if not discovered[current]:
                discovered[current]=True
                result.append(current)
            for neighbours in graph.data[current]:
                if not discovered[neighbours]:
                    stack.append(neighbours)
        return result
    def bfs(self, root):
        discovered=[False]*len(graph.data)
        discovered[root]=True
        queue=[]
        queue.append(root)
        result=[]

        while len(queue)!=0:
            current= queue.pop(0)
            result.append(current)
            for num in self.data[current]:
                if not discovered[num]:
                    discovered[num]=True 
                    queue.append(num)
        return result

# prodedure of bfs 
    # 1- let q be a queue
    # 2 label root as discovered 
    # 3 append root to queue
    # 4 while q is not empty do 
    # 5 deque the queue v=q.deque 
    # 6 if v is the goal then return v 
    # 7 else for all nums in self.data[v] do 
    # 8 if nums is not discovered then append nums 


            



        



graph=Graph(5,edges)
print(graph)
result=Graph.dfs(graph,3)
print(result)

