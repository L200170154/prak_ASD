class Pesan(object):
    """
        sebuah class bernama pesan.
        untuk memakai konsep class dan object.
    """
    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumKar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print("kalimatku mempunyai",len(self.teks),"karakter")
    def perbarui(self,stringBaru):
        self.teks = stringBaru
        
#nomor 1 a
    def apakahTerkandung(self, a):
        if str(a) in self.teks:
            return True
        else:
            return False
        
#nomor 1 b
    def hitungKonsonan(self):
        k="AUIEOauieo"
        jumlah=0
        for i in self.teks:
            if i not in k:
                jumlah+=1
        return jumlah
    
#nomor 1 c
    def hitungVokal(self):
        v="AUIEOauieo"
        jumlah=0
        for i in self.teks:
            if i in v:
                jumlah+=1
        return jumlah
    
class Manusia(object):
    """class 'Manusia' dengan inisiasi 'nama' """
    keadaan = "lapar"
    def __init__(self, nama):
        self.nama=nama
    def ucapkanSalam(self):
        print("Salam, namaku ",self.nama)
    def makan(self,s):
        print("Saya baru saja makan",s)
        self.keadaan="kenyang"
    def olahraga(self,k):
        print("Saya baru saja latihan", k)
        self.keadaan="lapar"
    def mengalikanDenganDua(self,n):
        return n*2

class Mahasiswa(Manusia):
    """class mahasiswa dibangun dari class manusia."""
    mataKuliah=[]
    def __init__(self,nama,NIM,kota,us):
        """metode inisiasi ini menutupi metode inisiasi di class manusia."""
        self.nama=nama
        self.NIM=NIM
        self.kotaTinggal=kota
        self.uangSaku=us
    def __str__(self):
        s=self.nama + ", NIM " + str(self.NIM)\
           + ". Tinggal di "+self.kotaTinggal\
           + ". Uang Saku "+str(self.uangSaku)\
           + " tiap bulannya."
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self,s):
        """metode ini menutupi metode 'makan'-nya di class manusia. mahasiswa kalau makan sambil belajar."""
        print("Saya baru saja makan",s,"sambil belajar.")
        self.keadaan="kenyang"
    def ambilKotaTinggal(self):
        return self.kotaTinggal

#nomor 2
    def perbaruiKotaTinggal(self,k):
        self.kotaTinggal=k
    def tambahUangSaku(self,n):
        self.uangSaku+=n

#nomor 4
    def ambilKuliah(self,mk):
        self.mataKuliah.append(mk)
    def listKuliah(self):
        print(self.mataKuliah)

#nomor 5
    def hapusKuliah(self,mk):
        return self.mataKuliah.remove(mk)
        
#nomor 3
nama=input("Masukan nama Anda      : ")
NIM=input("Masukan NIM Anda       : ")
kota=input("Masukan kota asal Anda : ")
us=input("Masukan uang saku Anda : ")

mx=Mahasiswa(nama,NIM,kota,us)

#nomor 6
class SiswaSMA(Manusia):
    jurusan="Belum ditentukan"
    universitas="Belum ditentukan"
    def __init__(self,nama,NISN,SMA):
        self.nama=nama
        self.nisn=NISN
        self.sma=SMA
    def __str__(self):
        s=self.nama + ", NISN " + str(self.nisn)\
           + ". Sekolah di "+self.sma
        return s
    def pilihanUniv(self):
        print ("Update Data")
        self.universitas=input("Masukan Universitas Pilihan : ")
        self.jurusan=input("Masukan Jurusan Pilihan : ")
    def tampilPilihan(self):
        print ("Pilihan Anda ",self.universitas," dengan Jurusan ",self.jurusan,".")
