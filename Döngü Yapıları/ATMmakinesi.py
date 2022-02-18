print("""
****************
ATM Makinesine Hoşgeldiniz
****************
Yapacağınız işlemi seçiniz
1-Bakiye Sorgula
2-Para Yatırma
3-Para Çekme
Çıkmak için q'a basınız
""")
bakiye = 10000

while True:
    islem = input("İşlemi Seçiniz")

    if(islem == "q"):
        print("Yine Bekleriz")
        break
    elif(islem == "1"):
        print("Bakiyeniz = {}".format(bakiye))
    elif (islem == "2"):
        miktar = int(input("Yatırmak istediğiniz miktar : "))
        bakiye += miktar
        print("Güncel Bakiye = {}".format(bakiye))
    elif(islem == "3"):
        cekilen = int(input("Çekmek istediğiniz miktar: "))
        if(bakiye < cekilen):
            print("Yetersiz Bakiye.")
            print("Bakiyeniz : {}".format(bakiye))
        else:
            bakiye -= cekilen
            print("Kalan bakiye = {}".format(bakiye))
    else:
        print("Yanlış İşlem Seçtiniz...")