class MhsTIF(object):
    def __init__(self, nama, nim, kota, us):
        self.nama=nama
        self.nim=nim
        self.kotaTinggal=kota
        self.uangSaku=us

    def __str__(self):
        x = self.nama + ', nim ' + str(self.umur) \
            + '. Tinggal di ' + self.kotaTinggal \
            + '. Uang saku ' + str(self.uangSaku) \
            + 'tiap bulannya.'
        return x

    def ambilNama(self):
        return self.nama
    def ambilUmur(self):
        return self.umur
    def ambilKota(self):
        return self.kotaTinggal
    def ambilUangSaku(self):
        return self.uangSaku

c0 = MhsTIF('Ika',10,'Sukoharjo',240000)
c1 = MhsTIF('Budi',51,'Sragen',230000)
c2 = MhsTIF('Ahmad',2,'Surakarta',250000)
c3 = MhsTIF('Chandra',18,'Surakarta',235000)
c4 = MhsTIF('Eka',4,'Boyolali',240000)
c5 = MhsTIF('Fandi',31,'Salatiga',250000)
c6 = MhsTIF('Deni',13,'Klaten',245000)
c7 = MhsTIF('Galuh',5,'Wonogiri',2450000)
c8 = MhsTIF('Janto',23,'Klaten',245000)
c9 = MhsTIF('Hasan',64,'Karanganyar',230000)
c10 = MhsTIF('Khalid',29,'Purwodadi',265000)

daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

#No1
def cariKota(x,target):
    z=[]
    for i in x:
        if i.kotaTinggal==target:
            hasil=x.index(i)
            z.append(hasil)
    return z

#No2
def cariTerkecil(x):
    n = len(x)
    terkecil=x[0].uangSaku
    for i in range(1,n):
        if x[i].uangSaku < terkecil:
            terkecil=x[i].uangSaku
    return terkecil

#No3 Error
def cariTerkecil2(x):
    n=len(x)
    z=[]
    terkecil=x[0].uangSaku
    for i in range(1,n):
        if x[i].uangSaku<terkecil:
            terkecil=x[i].uangSaku
        elif x[i].uangSaku==terkecil:
            z.append(x.index(i))
    return z

#No4
def cariBatas(x,target):
    b=[]  
    for i in x:
        if i.uangSaku<target:
            b.append(x.index(i))
    return b

#No5
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def pushAw(self, data_baru):
        node_baru = Node(data_baru)
        node_baru.next = self.head
        self.head = node_baru
    def pushAk(self, data):
        if(self.head == None):
            self.head = Node(data)
        else:
            current = self.head
            while (current.next != None):
                current = current.next
            current.next = Node(data)
        return self.head
    def insert(self, data, pos):
        node = Node(data)
        if not self.head:
            self.head = node
        elif posisi == 0:
            node.next = self.head
            self.head = node
        else:
            prev = None
            current = self.head
            current_pos = 0
            while(current_pos < pos) and current.next:
               prev = current
               current = current.next
               current_pos +=1
            prev.next = node
            node.next = current
        return self.head
    def search(self, v):
        current = self.head
        while current != None:
            if current.data == v:
                return "True"
            current = current.next
        return "False"
    def display(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next

#No6
def binSe(kumpulan, target):
    low = 0
    high = len(kumpulan) -1
    data = []
    while low <= high:
        mid = (high + low) //2
        if kumpulan[mid] == target:
            data.append(kumpulan.index(target))
            return True
        elif target < kumpulan[mid]:
            high = mid -1
        else :
            low = mid +1
    return False

#No7
def binSearch(kumpulan, target):
    low = 0
    high = len(kumpulan) -1
    data = []

    while low != high:
        mid = (high + low) //2
        if kumpulan[mid] == target:
            break
        elif target < kumpulan[mid]:
            high = mid -1
        else :
            low = mid +1
    for i in range (low, high):
        if target == kumpulan[i]:
            data.append(i)
    return data

a = [2,3,5,6,6,6,8,9,9,10,11,12,13,13,14]
