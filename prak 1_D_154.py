#nomor 1
def cetakSiku(x):
    for i in range(x):
        for j in range(i+1):
            print("*", end="")
        print()
cetakSiku(5)

#nomor 2
def gambarlahPersegiEmpat(a,b):
    for i in range(a):
        if i==0 or i==a-1:
            print("@"*b)
        else:
            print("@"+" "*(b-2)+"@")
gambarlahPersegiEmpat(4,5)

#nomor 3
def jumlahHurufVokal(kata):
    vokal="AUIEOauieo"
    jumlahvokal=""
    for k in kata:
        if k in vokal:
            jumlahvokal+=k
    print ("Jumlah huruf vokal : ",(len(jumlahvokal)))
    print ("Jumlah huruf : ",(len(kata)))
jumlahHurufVokal("Surakarta")

def jumlahHurufKonsonan(kata):
    vokal="AUIEOauieo"
    jumlahkonsonan=""
    for k in kata:
        if k not in vokal:
            jumlahkonsonan+=k
    print ("Jumlah huruf konsonan : ",(len(jumlahkonsonan)))
    print ("Jumlah huruf : ",(len(kata)))
jumlahHurufKonsonan("Surakarta")

#nomor 4
def rerata (rata=[]):
    hasil=sum(rata)/len(rata)
    print (hasil)
    return hasil
rerata([1,2,3,4,5])
g=[3,4,5,4,3,4,5,2,2,10,11,23]
rerata(g)

#nomor 5
from math import sqrt as sq
def apakahPrima(n):
    n=int(n)
    assert n>=0
    primaKecil=[2,3,5,7,11]
    bukanPrKecil=[0,1,4,6,8,9,10]
    if n in primaKecil:
        return True
    elif n in bukanPrKecil:
        return False
    else:
        for i in range(2,int(sq(n))+1):
            if(n%i==0):
                return False
    return True
print(apakahPrima(17))
print(apakahPrima(97))
print(apakahPrima(123))

#nomor 6
def printPrima():
    prima=list()
    for i in range(2,1000):
        a=True
        for iter in prima:
            if(i%iter==0):
                a=False
                break
        if(a):
            print(i)
            prima.append(i)
printPrima()

#nomor 7
def faktorPrima(y):
    prima=list()
    for i in range(2,y):
        a=True
        for iter in prima:
            if(i%iter==0):
                a=False
                break
        if a and y%i==0:
            prima.append(i)
    return prima
print(faktorPrima(10))

#nomor 8
def apakahTerkandung(a,b):
    return a in b
h="do"
k="Indonesia tanah air beta"
print(apakahTerkandung(h,k))

#nomor 9
def Iterasi():
    for i in range(1,100):
        if(i%3)!=0 and (i%5)!=0:
            print(i)
        else:
            if(i%15)==0:
                print("Python UMS")
            elif(i%3)==0:
                print("Python")
            elif(i%5)==0:
                print("UMS")
Iterasi()

#nomor 10
def selesaikanABC(a,b,c):
    a=float(a)
    b=float(b)
    c=float(c)
    d=(b**2)-(4*a*c)
    if d<0:
        return "Determinan negatif"
    return "Determinan positif"
print(selesaikanABC(1,2,3))

#nomor 11
def apakahKabisat(a):
    if(a%400==0):
        return True
    if(a%100==0):
        return False
    if(a%4==0):
        return True
    return False
print(apakahKabisat(1896))
print(apakahKabisat(1897))

#nomor 12
import random
def Permainan():
    a=random.randrange(0,100)
    while(True):
        b=int(input("Masukan tebakan : "))
        if(b>a):
              print("Itu terlalu besar. Coba lagi.")
        elif(b<a):
              print("Itu terlalu kecil. Coba lagi.")
        else:
              print("Ya. Anda benar")
              break
Permainan()

#nomor 13
def katakan(a):
    x={"0":"","1":"Se","2":"Dua ","3":"Tiga ","4":"Empat ","5":"Lima ","6":"Enam ","7":"Tujuh ","8":"Delapan ","9":"Sembilan "}
    y={-1:"",-2:"puluh ",-3:"ratus ",-4:"ribu ",-5:"puluh ",-6:"ratus ",-7:"juta ",-8:"puluhanjuta "}
    b=str(a)
    c=""
    i=-1
    while i>= -len(b):
        c=x[b[i]]+y[i]+c
        i-=1
    return c
print(katakan(3125750))

#nomor 14
def formatRupiah(a):
    b=str(a)
    c=""
    i=-1
    while i>=-len(b):
        if((i+1)%3==0 and (i+1)!=0):
            c="."+c
        c=b[i]+c
        i-=1
    return "Rp "+c
print(formatRupiah(1500))
