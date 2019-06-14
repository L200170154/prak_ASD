import re

f=open('Indonesia.txt','r',encoding='latin1')
teks=f.read()
f.close()

#nomor 1
xx=re.findall(r'me\w+',teks)
print(xx)

#nomor 2
rr=re.findall(r'di\w+',teks)
print(rr)

#nomor 3
pp=re.findall(r'di \w+',teks)
print(pp)

#nomor 4
wiki = open('KEI.htm', 'r', encoding='latin1')

teks = wiki.read()
wiki.close()


cari = re.findall(r'">([\w+]+)</a></td>\n<td>([0-9.]+)</td>\n<td>([0-9.]+)</td>\n<td>([0-9.]+)</td>\n<td>([0-9.]+)</td>\n<td>([0-9.]+)</td>\n<td>([0-9.]+)</td>', teks)

listbaru = []

for i in cari:
    a = (i[0],float(i[4]))
    listbaru.append(a)

print(listbaru)
