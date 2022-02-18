print("""
*******************
Hesap Makinesi Programı
İşlemler:
1- Toplama İşlemi
2- Çıkarma İşlemi
3- Çarpma İşlemi
4- Bölme İşlemi
*******************
""")
a = float(input("İlk Sayıyı Giriniz"))
b = float(input("İkinci Sayıyı Giriniz"))

islem = int(input("Yapılacak İşlemi Seçiniz"))

if islem == 1:
    print("{} ile {} in toplamı {}dir".format(a,b,a+b))
elif islem == 2:
    print("{} ile {} in farkı {}dir".format(a,b,a-b))
elif islem == 3:
    print("{} ile {} in çarpımı {}dir".format(a,b,a*b))
elif islem == 4:
    print("{} ile {} in bölümü {}dir".format(a,b,a/b))
else:
    print("Geçersiz İşlem!")
