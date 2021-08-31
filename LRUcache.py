class Node:
    def __init__(self,key=None,value=None):
        self.key=key
        self.value=value
        self.next=None
        self.prev=None

class LRUCache:
    def __init__(self,capacity):
        self.capacity=capacity
        self.hmp={}
        self.head=Node(-1,-1)
        self.tail=Node(-1,-1)
        self.head.next=self.tail
        self.tail.prev=  self.head
    
    def put(self,key,value):
        if key in self.hmp:
            self.__remove(self.hmp[key])
        
        if len(self.hmp) == self.capacity:
            self.__remove(self.tail.prev)    
        
        self.__insert(Node(key,value)) 
    
    def __insert(self,node):
        self.hmp[node.key]=node
        node.next=self.head.next
        node.next.prev=node
        self.head.next=node
        node.prev=self.head      
    
    def get(self,key):
        if key not in self.hmp:
            return -1
        node=self.hmp[key]
        self.__remove(node)
        self.__insert(node)
        return node.value       
     
    def __remove(self,node):
        self.hmp.pop(node.key)
        node.prev.next=node.next
        node.next.prev=node.prev
                  

if __name__=="__main__":
    lrucache=LRUCache(3)
    lrucache.put(1,1) 
    lrucache.put(2,2)
    lrucache.put(3,3)
    lrucache.put(4,4)
    print(lrucache.get(4))
    print(lrucache.get(3))
    print(lrucache.get(2))
    print(lrucache.get(1))
    lrucache.put(5,5)
    print(lrucache.get(1))
    print(lrucache.get(2))
    print(lrucache.get(3))
    print(lrucache.get(4))
    print(lrucache.get(5))
    
    
    # print(lrucache.get(2))
    # lrucache.get(3)
    
            
        
                 
                
        
            
        