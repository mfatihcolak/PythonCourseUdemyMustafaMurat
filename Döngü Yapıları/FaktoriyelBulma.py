print("""
*****************
Faktöriyel Hesaplama
*****************
Çıkmak için q'a basınız
""")

while True:
    sayi = input("Sayı:")
    if (sayi == "q"):
        print("Çıkış yapılıyor")
        break
    else:
        sayi = int(sayi)

        faktoriyel = 1

        for i in range(2,sayi+1):
            faktoriyel *= i
        print("Faktöriyel : ",faktoriyel)