import math
import Fonksiyonlar.OdevFonk2

print("""
Welcome my Calculator
Exit -> 'q'
Toplama -> 1
Çıkarma -> 2
Çarpma -> 3
Bölme -> 4
Mod Alma -> 5
Log -> 6
Log2 -> 7
Log 10 -> 8
Üs Alma -> 9
Kök -> 10
Sinüs Hesaplama -> 11
Kosinüs Hesaplama -> 12
EBOB - EKOK -> 13
""")

while True:
    islem = input("Lütfen yapmak istedğiniz işlemi seçiniz")
    if (islem == "q"):
        break
    elif (islem == "1"):
        a = int(input("1.sayıyı giriniz: "))
        b = int(input("2.sayıyı giriniz: "))
        print("Girdiğiniz sayıların toplamı = ", a + b)
    elif (islem == "2"):
        a = int(input("1.sayıyı giriniz: "))
        b = int(input("2.sayıyı giriniz: "))
        print("Girdiğiniz sayıların farkı = ", a - b)
    elif (islem == "3"):
        a = int(input("1.sayıyı giriniz: "))
        b = int(input("2.sayıyı giriniz: "))
        print("Girdğiniz sayıların çarpımı = ", a * b)
    elif (islem == "4"):
        a = int(input("1.sayıyı giriniz: "))
        b = int(input("2.sayıyı giriniz: "))
        if (b == 0):
            print("Payda'da 0 olmaz")
            break
        else:
            print("Girdiğiniz sayıların bölümü = ", a / b)
    elif (islem == "5"):
        a = int(input("1.sayıyı giriniz: "))
        b = int(input("2.sayıyı giriniz: "))
        print("Mod = ", math.fmod(a, b))
    elif (islem == "6"):
        a = int(input("1.sayıyı giriniz: "))
        b = int(input("2.sayıyı giriniz: "))
        print("{} log {} = {}".format(a, b, math.log(a, b)))
    elif (islem == "7"):
        c = int(input("Log2 hesabı için sayı giriniz: "))
        print("{} sayısının -> log2 tabanında eşiti = {}".format(c, math.log2(c)))
    elif (islem == "8"):
        c = int(input("Log10 hesabı için sayı giriniz: "))
        print("{} sayısının -> log10 tabanında eşiti = {}".format(c, math.log2(c)))
    elif (islem == "9"):
        a = int(input("1.sayıyı giriniz: "))
        b = int(input("2.sayıyı giriniz: "))
        print("{} üzeri {} = {}".format(a, b, math.pow(a, b)))
    elif (islem == "10"):
        a = int(input("1.sayıyı giriniz: "))
        b = int(input("2.sayıyı giriniz: "))
        print("{} kök {} = {}".format(a, b, math.sqrt(a, b)))
    elif (islem == "11"):
        c = int(input("Sinüsü hesaplanacak sayıyı radyan cinsinden giriniz:"))
        print("Sin = {}".format(math.sin(math.radians(c))))
    elif (islem == "12"):
        c = int(input("Kosinüsü hesaplanacak sayıyı radyan cinsinden giriniz:"))
        print("Cos = {}".format(math.cos(math.radians(c))))
    elif (islem == "13"):
        print(Fonksiyonlar.OdevFonk2.ebob())
    else:
        print("Yanlış işlem girdiniz")
