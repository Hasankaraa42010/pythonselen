
#vade=input("Kullanıcıdan giriş almak için")
#print(vade)
#alınan de"ğerleri türünü değiştirmek için

# değeri alırken direk istediğmizi veri türüne göre alma
#vade=int(input("Kullanıcıdan giriş almak için"))

#print("Seçtiğiniz vade:"+str(vade))
#print("Seçtriğiniz vade:{vadeSayisi}".format(vadeSayisi=vade))

isim="Halit"

metin="MERHABA {name}".format(name=isim)

print(metin)

#Fstring

metin=f"Hoşgeldiniz {isim}"
print(metin)

#list
krediler=["İhtiyaç","Taşıt"]

print(krediler)

print(len(krediler))

#listenin sonuna ekleme

krediler.append("özel")

print(krediler)

#istenilen elemanı silme

#krediler.pop(0)
#son elemanı silme
# krediler.pop()

#istenilen değeri silme(2 tane olursa ilki siler)

krediler.remove("Taşıt")
print(krediler)

#çoklu eleman ekleme diziye
krediler.extend(["Y kredisi","Z kredisi"])

print(krediler)


#for dongusu
#range kısmının içi ilk değer ve son değer olarak bakar ilk değer verilmesse 0 alır üçüncü değer ise artış sayısı
for i in range(10): 
    print(i)

# Foreach
for kredi in krediler:
    print(kredi)

print("While")
#while
# i=0
# while i<10:
#     print(i)
#     i+=1

#Fonksiyonlar
def calc(say,say2):
    print(say+say2)   
   
calc(5,7)
