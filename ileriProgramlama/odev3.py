import random
def prgram(*list):
    toplam=0
    metod=[0,1,2,3,4,5]
    for i in range(0,len(list)):
        sayi=random.randint(1,49)
        metod[i]=sayi
    for k in range(0,len(list)):
        for j in range(0,len(list)):
            if list[k]==metod[j]:
                toplam+=1
    return toplam
print(f"Tutan tahmin sayısı:{prgram(2,5,9,6,4,3)}")
