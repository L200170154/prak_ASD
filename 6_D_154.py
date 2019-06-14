from time import time as detak
from random import shuffle as kocok
import time
class MhsTIF():
    def __init__(self,nama,nim,kota,us):
        self.nama=nama
        self.nim=nim
        self.kota=kota
        self.us=us

c0=MhsTIF('Ika',10,'Sukoharjo',240000)
c1=MhsTIF('Budi',51,'Sragen',230000)
c2=MhsTIF('Ahmad',2,'Surakarta',250000)
c3=MhsTIF('Chandra',18,'Surakarta',235000)
c4=MhsTIF('Eka',4,'Boyolali',240000)
c5=MhsTIF('Fandi',31,'Salatiga',250000)
c6=MhsTIF('Deni',13,'Klaten',245000)
c7=MhsTIF('Galuh',5,'Wonogiri',245000)
c8=MhsTIF('Janto',23,'Klaten',245000)
c9=MhsTIF('Hasan',64,'Karanganyar',270000)
c10=MhsTIF('Khalid',29,'Purwodadi',265000)

daftar = [c0.nim, c1.nim, c2.nim, c3.nim, c4.nim, c5.nim, c6.nim, c7.nim, c8.nim, c9.nim, c10.nim]
xx=[2,6,12,13,1,3,4]

#nomor 1
def mergeSort(A):
    if len(A)>1:
        mid = len(A)//2
        separuhKiri=A[:mid]
        separuhKanan=A[mid:]

        mergeSort(separuhKiri)
        mergeSort(separuhKanan)

        i=0;j=0;k=0
        while i<len(separuhKiri) and j<len(separuhKanan):
            if separuhKiri[i]<separuhKanan[j]:
                A[k]=separuhKiri[i]
                i+=1
            else:
                A[k]=separuhKanan[j]
                j+=1
            k+=1
        while i<len(separuhKiri):
            A[k]=separuhKiri[i]
            i+=1
            k+=1
        while j<len(separuhKanan):
            A[k]=separuhKanan[j]
            j+=1
            k+=1

def partisi(A,awal,akhir):
    nilaiPivot=A[awal]
    penandaKiri=awal+1
    penandaKanan=akhir

    selesai=False
    while not selesai:
        while penandaKiri<=penandaKanan and A[penandaKiri]<=nilaiPivot:
            penandaKiri+=1

        while A[penandaKanan]>=nilaiPivot and penandaKanan>=penandaKiri:
            penandaKanan+=1

        if penandaKanan<penandaKiri:
            selesai=True
        else:
            temp=A[penandaKiri]
            A[penandaKiri]=A[penandaKanan]
            A[penandaKanan]=temp
    temp=A[awal]
    A[awal]=A[penandaKanan]
    A[penandaKanan]=temp

    return penandaKanan

def quickSortBantu(A,awal,akhir):
    if awal<akhir:
        titikBelah=partisi(A,awal,akhir)
        quickSortBantu(A,awal,titikBelah-1)
        quickSortBantu(A,titikBelah+1,akhir)

def partisi(A,awal,akhir):
    nilaiPivot=A[awal]
    penandaKiri=awal+1
    penandaKanan=akhir

    selesai=False
    while not selesai:
        while penandaKiri<=penandaKanan and A[penandaKiri]<=nilaiPivot:
            penandaKiri+=1

        while A[penandaKanan]>=nilaiPivot and penandaKanan>=penandaKiri:
            penandaKanan-=1

        if penandaKanan<penandaKiri:
            selesai=True
        else:
            temp=A[penandaKiri]
            A[penandaKiri]=A[penandaKanan]
            A[penandaKanan]=temp
    temp=A[awal]
    A[awal]=A[penandaKanan]
    A[penandaKanan]=temp

    return penandaKanan

def quickSort(A):
    quickSortBantu(A,0,len(A)-1)

#nomor 3
def bubbleSort(A):
    n=len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]
    print (A)
    
def selectionSort(A):
    for i in range(len(A)):
        indexKecil=i
        for j in range(i+1,len(A)):
            if A[indexKecil]>A[j]:
                indexKecil=j
        A[j],A[indexKecil]=A[indexKecil],A[j]
    print (A)

def insertionSort(A):
    n=len(A)
    for i in range(1,n):
        nilai=A[i]
        pos=i
        while pos>0 and nilai<A[pos-1]:
            A[pos]=A[pos-1]
            pos-=1
        A[pos]=nilai
    print (A)

k=[i for i in range(1,6001)]
kocok(k)
u_bub=k[:]
u_sel=k[:]
u_ins=k[:]
u_mrg=k[:]
u_qck=k[:]

aw=detak();bubbleSort(u_bub);ak=detak();print('bubble: %g detik' %(ak-aw));
aw=detak();selectionSort(u_sel);ak=detak();print('selection: %g detik' %(ak-aw));
aw=detak();insertionSort(u_ins);ak=detak();print('insertion: %g detik' %(ak-aw))
aw=detak();mergeSort(u_mrg);ak=detak();print('merge: %g detik' %(ak-aw))
aw=detak();quickSort(u_qck);ak=detak();print('quick: %g detik' %(ak-aw))

#nomor 5
import random
def _merge_sort(indices, the_list):
    start = indices[0]
    end = indices[1]
    half_way = (end - start)//2 + start
    if start < half_way:
        _merge_sort((start, half_way), the_list)
    if half_way + 1 <= end and end - start != 1:
       _merge_sort((half_way + 1, end), the_list)

    sort_sub_list(the_list, indices[0], indices[1])
    return the_list
    
    
def sort_sub_list(the_list, start, end):
    orig_start = start
    initial_start_second_list = (end - start)//2 + start + 1
    list2_first_index = initial_start_second_list
    new_list = []
    while start < initial_start_second_list and list2_first_index <= end:
        first1 = the_list[start]
        first2 = the_list[list2_first_index]
        if first1 > first2:
            new_list.append(first2)
            list2_first_index += 1
        else:
            new_list.append(first1)
            start += 1
    while start < initial_start_second_list:
        new_list.append(the_list[start])
        start += 1

    while list2_first_index <= end:
        new_list.append(the_list[list2_first_index])
        list2_first_index += 1
    for i in new_list:
        the_list[orig_start] = i
        orig_start += 1
    return the_list


def merge_sort(the_list):
    return _merge_sort((0, len(the_list) - 1), the_list)

print(merge_sort([13,45,12]))

#nomor 6
def quickSort(L, ascending = True): 
    quicksorthelp(L, 0, len(L), ascending)
    
def quicksorthelp(L, low, high, ascending = True): 
    result = 0
    if low < high: 
        pivot_location, result = Partition(L, low, high, ascending)  
        result += quicksorthelp(L, low, pivot_location, ascending)  
        result += quicksorthelp(L, pivot_location + 1, high, ascending)
    return result


def Partition(L, low, high, ascending = True):
    result = 0 
    pivot, pidx = median_of_three(L, low, high)
    L[low], L[pidx] = L[pidx], L[low]
    i = low + 1
    for j in range(low+1, high, 1):
        result += 1
        if (ascending and L[j] < pivot) or (not ascending and L[j] > pivot):
            L[i], L[j] = L[j], L[i]  
            i += 1
    L[low], L[i-1] = L[i-1], L[low] 
    return i - 1, result

def median_of_three(L, low, high):
    mid = (low+high-1)//2
    a = L[low]
    b = L[mid]
    c = L[high-1]
    if a <= b <= c:
        return b, mid
    if c <= b <= a:
        return b, mid
    if a <= c <= b:
        return c, high-1
    if b <= c <= a:
        return c, high-1
    return a, low

liste1 = list([1,3,2,16,20,11])

quickSort(liste1, False)
print('sorted:')
print(liste1)

#nomor 7
mer = k[:]
qui = k[:]
mer2 = k[:]
qui2 = k[:]


aw=detak();mergeSort(mer);ak=detak();print('merge : %g detik' %(ak-aw));
aw=detak();quickSort(qui,0,len(qui)-1);ak=detak();print('quick : %g detik' %(ak-aw));
aw=detak();merge_sort(mer2);print('merge mod : %g detik' %(ak-aw));
aw=detak();quickSortMOD(qui2, False);print('quick mod : %g detik' %(ak-aw));

#nomor 8
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def appendList(self, data):
    node = Node(data)
    if self.head == None:
      self.head = node
    else:
      curr = self.head
      while curr.next != None:
        curr = curr.next
    curr.next = node

  def appendSorted(self, data):
    node = Node(data)
    curr = self.head
    prev = None

    while curr is not None and curr.data < data:
      prev = curr
      curr = curr.next
		
    if prev == None:
      self.head = node
    else:
      prev.next = node

    node.next = curr

  def printList(self):
    curr = self.head
    while curr != None:
      print ("%d"%curr.data),
      curr = curr.next
  def mergeSorted(self, list1, list2):
    if list1 is None:
      return list2
    if list2 is None:
      return list1

    if list1.data < list2.data:
      temp = list1
      temp.next = self.mergeSorted(list1.next, list2)
    else:
      temp = list2
      temp.next = self.mergeSorted(list1, list2.next)
    return temp
					

list1 = LinkedList()
list1.appendSorted(4)
list1.appendSorted(3)
list1.appendSorted(5)
list1.appendSorted(1)
list1.appendSorted(10)

print("List 1 :"),
list1.printList()

list2 = LinkedList()
list2.appendSorted(6)
list2.appendSorted(12)
list2.appendSorted(2)

print("List 2 :"),
list2.printList()

list3 = LinkedList()
list3.head = list3.mergeSorted(list1.head, list2.head)

print("Merged List :"),
list3.printList()
