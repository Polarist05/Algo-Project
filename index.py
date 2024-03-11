from queue import PriorityQueue
from MyHeap import MyHeap as Heap
def recieveInput():
    edges:list[tuple[int,int,int]] = []
    nodeCount = int(input("Input Node Numbers : "))
    edgeCount = int(input("Input Edge Numbers : "))
    print('Input each edge by (start , end , weight) with seperate by space')
    for i in range(edgeCount) :
        start,end,weight= [int(s) for s in input('Edge {0} : '.format(i)).split()]
        start-=1
        end-=1
        edges.append((start,end,weight))
    return {
        'nodeCount':nodeCount,
        'edges':edges
    }

# Minimum Except Node 2
# Node Count from 0 - (N-1)
# Edge Tuple (Start_Node,End_Node,Weight)
# Node_Count< Edges_Length < Node_Count^2
# Edge must not connect same node Ex 0-1 1-0
# Graph must be fully connect
# Weight > 0

def getMaximumWeight(nodeCount:int,inpEdges:list[tuple[int,int,int]]):
    edges:dict[int,list[int,int,int]] = {}
    traverseEdge = [-1 for i in range(nodeCount)]
    verts = set(range(nodeCount))
    weight = [-999999999 for i in range(nodeCount)]
    hp = Heap(nodeCount,lambda a,b : a>b)

    for i in range(len(inpEdges)):
        start,end,w = inpEdges[i]
        start,end = min(start,end),max(start,end)
        if start not in edges:
            edges[start] = []
        if end not in edges:
            edges[end] = []
        edges[start].append((end,w,i))
        edges[end].append((start,w,i))
    hp.push(-1,0)
    while(len(verts)>0):
        key,val = hp.pop()
        verts.remove(val)
        for neighbor,w,index in edges[val]:
            if neighbor in verts and w > weight[neighbor]:
                traverseEdge[neighbor] = index
                weight[neighbor] = w
                hp.push(w,neighbor)
    for index in traverseEdge:
        if index > -1:
            inpEdges[index] = (-1,-1,-1)
    notUseEdges = [edge[2] for edge in inpEdges ]
    return max(notUseEdges) if len(notUseEdges) >0 else -1
      

if __name__ == '__main__':
    inp = recieveInput()
    print("result :",getMaximumWeight(inp['nodeCount'],inp['edges']))
