from queue import PriorityQueue
def recieveInput():
    edges:list[tuple[int,int,int]] = []
    nodeCount = int(input("Input Node Numbers : "))
    startNode = int(input("Input Start Node : ")) - 1
    edgeCount = int(input("Input Edge Numbers : "))
    for i in range(edgeCount) :
        start,end,weight= [int(s) for s in input('Edge {0} : '.format(i)).split()]
        start-=1
        end-=1
        edges.append((start,end,weight))
    return {
        'nodeCount':nodeCount,
        'startNode':startNode,
        'edges':edges
    }

# Minimum Except Node 2
# Node Count from 0 - (N-1)
# Edge Tuple (Start_Node,End_Node,Weight)
# Node_Count< Edges_Length < Node_Count^2
# Edge must not connect same node Ex 0-1 1-0
# Graph must be fully connect
# Weight > 0
class MyHeap():
    def __init__(self,size) -> None:
        self.data = []
        self.key = []
        self.index = [-1 for i in range(size)]
    def size(self):
        return len(self.data)  
    def push(self,key,value):
        if self.index[value] == -1:
            self.data.append(value)
            self.key.append(key)
            self.index[value] = self.size()-1
            self.bubbleUp(self.size()-1)
        else:
            self.decreaseKey(value,key)
    def pop(self):
        result = (self.key[0],self.data[0])
        self.swap(0,self.size()-1)
        self.data.pop()
        self.key.pop()
        self.bubbleDown(0)
        return result
    def decreaseKey(self,value,newKey):
        index = self.index[value] 
        if(newKey < self.key[index]):
            self.key[index] = newKey
            self.bubbleUp(index)
    def swap(self,index1,index2):
        self.data[index1],self.data[index2] = self.data[index2],self.data[index1]
        self.key[index1],self.key[index2] = self.key[index2],self.key[index1]
        self.index[self.data[index1]],self.index[self.data[index2]] = index1,index2
    def bubbleUp(self,index):
        parent = (index-1)//2
        if(index>0 and self.key[index]<self.key[parent]):
            self.swap(index,parent)
            index = parent
            self.bubbleUp(parent)
    def bubbleDown(self,index):
        child1,child2 = index*2+1,index*2+2
        size =len(self.key)
        if child2<size:
            if self.key[child1] < self.key[index] and self.key[child1] < self.key[child2]:
                self.swap(index,child1)
                index = child1
                self.bubbleDown(child1)
            if self.key[child2] < self.key[index] and self.key[child2] < self.key[child1]:
                self.swap(index,child2)
                index = child2
                self.bubbleDown(child2)
        elif child1<size and self.key[child1] < self.key[index]:
            self.swap(index,child1)
            index = child1
            self.bubbleDown(child1)

def getPrimAlgorithm(nodeCount:int,inpEdges:list[tuple[int,int,int]]):
    result = -1000
    edges:dict[int,list[int,int]] = {}
    for start,end,w in inpEdges:
        if start not in edges:
            edges[start] = []
        if end not in edges:
            edges[end] = []
        edges[start].append((end,w))
        edges[end].append((start,w))
    verts = set(range(nodeCount))
    weight = [999999999 for i in range(nodeCount)]
    hp = MyHeap(nodeCount)
    hp.push(-1,0)
    while(len(verts)>0):
        key,val = hp.pop()
        verts.remove(val)
        result = max(result,key)
        for neighbor,w in edges[val]:
            if neighbor in verts and w < weight[neighbor]:
                weight[neighbor] = w
                hp.push(w,neighbor)
    cnt = 0
    for _,_,w in inpEdges:
        result2=999999999
        if w<=result:
            cnt+=1
        elif result2 > w:
            result2 = w
    if cnt != nodeCount-1:
        return result
    elif cnt == len(inpEdges):
        return -1
    else:
        return result2
        

if __name__ == '__main__':
    print(getPrimAlgorithm(3,[
        [0,1,2],
        [1,2,3]
    ]))
def findAtLeastCost(nodeCount:int,startNode:int,edges:list[tuple[int,int,int]]):
    edgeLen = len(edges)
    pq:PriorityQueue[tuple[int,int,int]] = PriorityQueue()
    edgesAtNode:dict[int,list[tuple[int,int,int]]] = {}
    nodeTraverse:list[bool] = [False for i in range(nodeCount)]
    edgeTraverse:list[bool] = [False for i in edges]
    #Define Value Edge_At_Node
    for i in range(edgeLen):
        start,end,weight = edges[i]        
        if start not in edgesAtNode.keys():
            edgesAtNode[start] = []
        if end not in edgesAtNode.keys():
            edgesAtNode[end] = []
        edgesAtNode[start].append((end,weight,i))
        edgesAtNode[end].append((start,weight,i))
    #Setup
    nodeTraverse[startNode] = True
    for end,weight,id in edgesAtNode[startNode]:
        pq.put((-weight,end,id))
    #Loop Spanning Tree
    while(not pq.empty()):
        _,start,id=pq.get()
        if not nodeTraverse[start]:
            for end,weight,id2 in edgesAtNode[start]:
                if not nodeTraverse[end]:
                    pq.put((-weight,end,id2))
            edgeTraverse[id] = True
            nodeTraverse[start] = True
    #Find result
    result = [edges[i][2] for i in range(edgeLen)if not edgeTraverse[i]]
    return max(result) if len(result)>0 else 0

