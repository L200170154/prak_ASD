#nomor 4
class Queue(object):
    def __init__(self):
        self.qlist = []
    def isEmpty(self):
        return len(self)==0
    def __len__(self):
        return len(self.qlist)
    def enqueue(self,data):
        self.qlist.append(data)
    def dequeue(self):
        assert not self.isEmpty()
        return self.qlist.pop(0)
    def getFront(self):
        return self.qlist[-1]
    def getRear(self):
        return self.qlist[0]

a = Queue()
a.enqueue('Batu')
a.enqueue('Kayu')
a.enqueue('Kulit')

print('Queue')
print(a.qlist)
print(a.getFront())
print(a.getRear())

import heapq
class Prior(object):
    def __init__(self):
        self.qlist= []
    def __len__(self):
        return len(self.qlist)
    def isEmpty(self):
        return len(self)==0
    def enqueue(self, data, prior):
        heapq.heappush(self.qlist, (prior, data))
        self.qlist.sort()
    def dequeue(self):
        return self.qlist.pop(-1)
    def getFront(self):
        return self.qlist[-1]
    def getRear(self):
        return self.qlist[0]
    
b = Prior()

b.enqueue('Batu', 5)
b.enqueue('Kayu', 1)
b.enqueue('Kulit', 2)

print('''
Priority Queue''')
print(b.qlist)
print(b.getFront())
print(b.getRear())

#nomor 5
c = Prior()

c.enqueue('Batu',5)
c.enqueue('Kayu',1)
c.enqueue('Kulit',2)

print(c.qlist)
c.dequeue()
print(c.qlist)
