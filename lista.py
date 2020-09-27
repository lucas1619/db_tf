from nodo import Node
import gc
class DoubleLinkedList:
    def __init__(self):
        self.start = Node()
        self.end = Node()
        self.size = 0
    def __len__(self):
      return self.size
    def __contains__(self, value):
      aux = self.start
      while aux != None:
        if aux.value == value:
          return True
        aux = aux.next
      return False      
    def __iter__(self):
        node = self.start
        while node:
            yield node.value
            node = node.next
    def push_front(self, value):
      new = Node(value)
      if self.size == 0:
        self.start = self.end = new
        self.size += 1
        return
      new.next = self.start
      self.start.prev = new
      self.start = new
      self.size += 1
    def push_back(self, value):
      if self.size == 0:
        self.push_front(value)
        return  
      new = Node(value)
      self.end.next = new
      new.prev = self.end
      self.end = new
      self.size += 1
    def insert(self, index, value):
      if self.size == 0 or index == 0:
        self.push_front(value)
        return  
      if index == self.size - 1:
        self.push_back(value)
        return
      if index < 0 or index >= self.size:
        return
      new = Node(value)
      c = self.start
      for i in range(index - 1):
        c = c.next
      new.next = c.next
      c.next.prev = new
      c.next = new
      new.prev = c
      self.size += 1
    def pop_back(self):
      if self.size <= 0:
        return
      if self.size == 1:
        self.start = self.end = None
        self.size -= 1
        gc.collect()
        return
      self.end = self.end.prev
      self.end.next.prev = None
      self.end.next = None
      self.size -= 1
      gc.collect()
    def pop_front(self):
      if self.size <= 1:
        self.pop_back()
        return
      self.start = self.start.next
      self.start.prev.next = None
      self.start.prev = None
      self.size -= 1
      gc.collect()
    def delete(self, index):
      self.size -= 1
    def erase(self,pos):
        if pos < self.size and pos >=0:
            if(pos==0):
                self.eliminaralinicio()
            elif pos == self.size :
                self.eliminaralfinal()
            else:        
                punt = self.start
                contador=0
                while(contador !=pos -1):
                  punt = punt.next
                  contador+=1
                  elimi= punt.next
                punt.next = elimi.next
                elimi.next =None
                del elimi
                self.size -= 1
        gc.collect()        