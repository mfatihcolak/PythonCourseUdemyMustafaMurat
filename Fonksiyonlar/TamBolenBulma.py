def tamBolenBulma(a):
    tamBolenler = []

    for i in range(2,a):
        if(a%i == 0):
            tamBolenler.append(i)
    return tamBolenler
while True:
    print("Çıkmak için q'a basınız..")
    sayi = input("Sayı:")

    if(sayi == "q"):
        break
    else:
        sayi = int(sayi)
        print("tam bölenler: ",tamBolenBulma(sayi))