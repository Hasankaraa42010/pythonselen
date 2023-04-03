import random
sifreler=[]
buyukharf=["A","B","C","D","E","F","G"]
kucukharf=["a","b","c","d","e","f","g"]

ozelkarakter=["!","&","^","?","#","$"]
rakam=[0,1,2,3,4,5,6,7,8,9]
rastgeleSayilar=[]
rastgeleSayilar.extend(buyukharf)
rastgeleSayilar.extend(kucukharf)
rastgeleSayilar.extend(ozelkarakter)
rastgeleSayilar.extend(rakam)
for i in range(0,100):
    sifre=kucukharf[random.randint(0,6)]+buyukharf[random.randint(0,6)]+str(rakam[random.randint(0,9)])+str(ozelkarakter[random.randint(0,len(ozelkarakter)-1)])+str(rastgeleSayilar[random.randint(0,len(rastgeleSayilar)-1)])+str(rastgeleSayilar[random.randint(0,len(rastgeleSayilar)-1)])+str(rastgeleSayilar[random.randint(0,len(rastgeleSayilar)-1)])+str(rastgeleSayilar[random.randint(0,len(rastgeleSayilar)-1)])
    sifreler.append(sifre)


    
for i in range(0,len(sifreler)):
    sifre1=str(sifreler[i])
    koruma=[]
    toplam=0
    for a in range(0,8):
        koruma.append(sifre1[a:a+1])
        
    for j in range(0,10):
        for c in range(0,8):
            if koruma[c]==str(rakam[j]):
                toplam+=1
    
    if toplam>2:
        print(f"Hata {sifreler[i]} da toplam{toplam} adet rakam var")