class MyHeap():
    def __init__(self,size,comp = lambda a,b: a<b) -> None:
        self.data = []
        self.key = []
        self.index = [-1 for i in range(size)]
        self.comp = comp
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
        if(self.comp(newKey , self.key[index])):
            self.key[index] = newKey
            self.bubbleUp(index)
    def swap(self,index1,index2):
        self.data[index1],self.data[index2] = self.data[index2],self.data[index1]
        self.key[index1],self.key[index2] = self.key[index2],self.key[index1]
        self.index[self.data[index1]],self.index[self.data[index2]] = index1,index2
    def bubbleUp(self,index):
        parent = (index-1)//2
        if(index>0 and self.comp(self.key[index],self.key[parent]) ):
            self.swap(index,parent)
            index = parent
            self.bubbleUp(parent)
    def bubbleDown(self,index):
        child1,child2 = index*2+1,index*2+2
        size =len(self.key)
        if child2 <size:
            if self.comp(self.key[child1] , self.key[index])  and self.comp(self.key[child1] , self.key[child2]) :
                self.swap(index,child1)
                index = child1
                self.bubbleDown(child1)
            if self.comp(self.key[child2] , self.key[index])  and self.comp(self.key[child2] , self.key[child1]) :
                self.swap(index,child2)
                index = child2
                self.bubbleDown(child2)
        elif child1 < size  and self.comp(self.key[child1] , self.key[index]) :
            self.swap(index,child1)
            index = child1
            self.bubbleDown(child1)
