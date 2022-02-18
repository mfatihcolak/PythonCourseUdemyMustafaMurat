import random
import time

print("""
SAYI TAHMİN OYUNU
1-40 ARASI SAYIYI TAHMİN EDİN
""")

rastgeleSayi = random.randint(1,40)
hak = 7

while True:
    tahmin = int(input("Tahmininiz :"))
    if(tahmin < rastgeleSayi):
        print("Bilgiler sorgulanıyor")
        time.sleep(1)
        print("Daha Yüksek")
        hak -=1
        print("Kalan hakkınız = ",hak)
    elif(tahmin > rastgeleSayi):
        print("Bilgiler sorgulanıyor")
        time.sleep(1)
        print("Daha düşük")
        hak -=1
        print("Kalan hakkınız = ", hak)
    else:
        print("Bilgiler doğrulanıyor")
        time.sleep(1)
        print("TEBRİKLER SAYINIZ = ",rastgeleSayi)
    if(hak == 0):
        print("Tahmin hakkınız bitti..")
        break