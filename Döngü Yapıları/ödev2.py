print("Çıkış için q'a basınız..")
toplam = 0

while True:
    islem = input("Toplamak istedğiniz sayıları giriniz")

    if (islem == "q"):
        break
    islem = int(islem)
    toplam = toplam + islem
    print(toplam)


