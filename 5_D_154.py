from time import time as detak
from random import shuffle as kocok

#1
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

daftar = [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]
xx=[2,6,12,13,1,3,4]
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

#2 
A=[2,4,10,18,31,51]
B=[5,13,23,29,64]
def gabung(A,B):
    la=len(A); lb=len(B)
    C=list()
    i=0; j=0

    while i<la and j<lb:
        if A[i]<B[j]:
            C.append(A[i])
            i+=1
        else:
            C.append(B[j])
            j+=1

    while i<la:
        C.append(A[i])
        i+=1
    while i<lb:
        C.append(B[j])
        j+=1

    return C

#3
k=[i for i in range(1,6001)]
kocok(k)
u_bub=k[:]
u_sel=k[:]
u_ins=k[:]

aw=detak();bubbleSort(u_bub);ak=detak();print('bubble: %g detik' %(ak-aw));
aw=detak();selectionSort(u_sel);ak=detak();print('selection: %g detik' %(ak-aw));
aw=detak();insertionSort(u_ins);ak=detak();print('insertion: %g detik' %(ak-aw));
