class Stack():
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return len(self)==0
    def __len__(self):
        return len(self.items)
    def peek(self):
        assert not self.isEmpty()
        return self.items[-1]
    def pop(self):
        assert not self.isEmpty()
        return self.items.pop()
    def push(self, data):
        return self.items.append(data)

#nomor 1
def cetakHexa(data):
    hx = Stack()
    hxlist = "0123456789ABCDEF"
    while data != 0:
        sisa = data%16
        data = data//16
        hx.push(hxlist[sisa])
    st=""
    for i in range(len(hx)):
        st = st + str(hx.pop())
    return st

print(cetakHexa(12))
print(cetakHexa(31))
print(cetakHexa(229))
print(cetakHexa(255))
print(cetakHexa(31519))

#nomor 2
nilai=Stack()
for i in range(16):
    if i%3==0:
        nilai.push(i)
        print(nilai.items)

#nomor 3
nilai=Stack()
for i in range(16):
    if i%3==0:
        nilai.push(i)
    elif i%4==0:
        nilai.pop()
print(nilai.items)


