#1
a=[[1,2],[3,4]]
b=[[1,2],[3,4],[5,6]]
c=[[1,"a"],[2,4]]
d=[[1,1],[2,2]]
def Konsisten(n):
    x=len(n[0])
    y=0
    for i in range(len(n)):
        if(len(n[i])==x):
            y+=1
    if(y==len(n)):
        print("Matriks Konsisten")
    else:
        print("Matriks Tidak Konsisten")
Konsisten(a)

def cekIsi(n):
    x=0
    y=0
    for i in n:
        for j in i:
            y+=1
            if (str(j).isdigit()==False):
                print("Tidak semua isi matriks adalah angka")
                break
            else:
                x+=1
    if(x==y):
        print("Semua isi matriks adalah angka")
cekIsi(a)

def Ukuran(n):
    x=0
    y=0
    for i in range(len(n)):
        x+=1
        y=len(n[i])
    print("Matriks mempunyai ordo "+str(x)+"x"+str(y))
Ukuran(a)
Ukuran(b)

def Jumlah(n,m):
    x=0
    y=0
    z=0
    for i in range(len(n)):
        x+=1
        y=len(n[i])
    xy=[[0 for j in range(x)] for i in range(y)]

    if(len(n)==len(m)):
        for i in range(len(n)):
            if(len(n[i])==len(m[i])):
               z+=1
    if(z==len(n) and z==len(m)):
        print("Ukuran matriks sama")
        for i in range(len(n)):
            for j in range(len(n[i])):
                xy[i][j]=n[i][j]+m[i][j]
        print(xy)        
    else:
        print("Ukuran matriks berbeda")
Jumlah(a,b)

def Kali(n,m):
    a=0
    x=0
    y=0
    for i in range(len(n)):
        x+=1
        y=len(n[i])
    v=0
    w=0
    for i in range(len(m)):
        v+=1
        w=len(m[i])

    if(y==v):
        print("Matriks dapat dikalikan")
        hasil=[[0 for j in range(w)] for i in range(x)]
        for i in range(len(n)):
            for j in range(len(m[0])):
                for k in range(len(m)):
                    hasil[i][j]+=n[i][k]*m[k][j]
        print(hasil)
    else:
        print("Matriks tidak memenuhi syarat")

Kali(a,d)
xa=[[1,2,3],[2,3,4],[3,4,1]]
xb=[[1],[2],[3]]
Kali(xa,xb)

def hitungDet(n, total=0):
    x=len(n[0])
    y=0
    for i in range(len(n)):
        if(len(n[i])==x):
            y+=1
    if(y==len(n)):
        if(x==len(n)):
            indices=list(range(len(n)))
            if len(n)==2 and len(n[0])==2:
                val=n[0][0]*n[1][1]-n[1][0]*n[0][1]
                return val
            for fc in indices:
                ns=n
                ns=ns[1:]
                height=len(ns)
                for i in range(height):
                    ns[i]=ns[i][0:fc]+ns[i][fc+1:]
                sign=(-1)**(fc%2)
                sub_det=hitungDet(ns)
                total+=sign*n[0][fc]*sub_det
        else:
            return "Tidak dapat dihitung, bukan matrix bujursangkar"
    else:
        return "Tidak dapat dihitung, bukan matrix bujursangkar"
    return total

print(hitungDet(a))
print(hitungDet(b))

#2
def buatNol(n,m=None):
    if(m==None):
        m=n
    print("membuat matrix 0 dengan ordo "+str(n)+"x"+str(m))
    print([[0 for j in range(m)] for i in range(n)])

buatNol(2,3)
buatNol(3)

def buatIdentitas(n):
    print("Membuat matrix identitas dengan ordo "+str(n)+"x"+str(n))
    print([[1 if j==i else 0 for j in range(n)] for i in range(n)])

buatIdentitas(2)
buatIdentitas(3)

#3
class Node:
    def __init__(self,data):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None
    def pushAwal(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def pushAkhir(self,data):
        if(self.head==None):
            self.head=Node(data)
        else:
            current=self.head
            while(current.next!=None):
                current=current.next
            current.next=Node(data)
        return self.head
    def Insert(self,data,posisi):
        node=Node(data)
        if not self.head:
            self.head=node
        elif posisi==1:
            node.next=self.head
            self.head=node
        else:
            prev=None
            current=self.head
            current_pos=0
            while(current_pos<posisi)and current.next:
                prev=current
                current=current.next
                current_pos+=1
            prev.next=node
            node.next=current
        return self.head
    def Delete(self,pos):
        if self.head==None:
            return
        temp=self.head
        if pos==0:
            self.head=temp.next
            temp=None
            return
        for i in range(pos -1):
            temp=temp.next
            if temp is None:
                break
        if temp is None:
            return
        if temp.next is None:
            return
        next=temp.next.next
        temp.next=None
        temp.next=next
    def Search(self,cari):
        current=self.head
        while current != None:
            if current.data==cari:
                return "True"
            current=current.next
        return "False"
    def Display(self):
        current=self.head
        while current is not None:
            print(current.data, end=' ')
            current=current.next

llist=LinkedList()
llist.pushAwal(21)
llist.pushAwal(22)
llist.pushAwal(12)
llist.pushAwal(14)
llist.pushAwal(2)
llist.pushAwal(19)
llist.pushAkhir(9)
llist.Delete(0)
llist.Insert(1,6)
print(llist.Search(21))
llist.Display()

#4
class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    def awal(self, new_data):
        print("Menambah pada awal",new_data)
        new_node=Node(new_data)
        new_node.next=self.head
        if self.head is not None:
            self.head.prev=new_node
        self.head=new_node
    def akhir(self,new_data):
        print("Menambah pada akhir",new_data)
        new_node=Node(new_data)
        new_node.next=None
        if self.head is None:
            new_node.prev=None
            self.head=new_node
            return
        last=self.head
        while(last.next is not None):
            last=last.next
        last.next=new_node
        new_node.prev=last
        return
    def printList(self,node):
        print("\nDari depan :")
        while(node is not None):
            print("%d"%(node.data))
            last=node
            node=node.next
        print("\Dari belakang :")
        while(last is not None):
            print("%d"%(last.data))
            last=last.prev
db=DoublyLinkedList()
db.awal(7)
db.awal(1)
db.akhir(6)
db.akhir(4)
db.printList(db.head)
