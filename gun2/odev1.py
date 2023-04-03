list1=["Kerata","Hasan kara"]

def ekle(isim):
    list1.append(isim)

def delete(isim):
    list1.remove(isim)

def cokluEkleme(*params):
    for i in params:
        list1.append(i)
        
def indexNumarasiOgrenme(isim):
    for i in range(len(list1)):
        if list1[i]==isim:
            print(f"Öğrenci numarası:{i}")   

def cokluSilme(*params):
    for i in params:
        list1.remove(i)

def listleme():
    i=0
    while i<len(list1):
         print(f"Öğrenci:{list1[i]}")     
         i+=1       

cokluEkleme("Polat","Memati")
print(list1)

print("Öğrenci numarasına göre getirtme")
print("--------------------------------")
isim=input("Öğrenmek istedğininiz öğrenci adını girin")
indexNumarasiOgrenme(isim)



