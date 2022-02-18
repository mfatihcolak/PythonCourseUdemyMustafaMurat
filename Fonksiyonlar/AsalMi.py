def asalMi(a):
    if(a == 1):
        return False
    elif(a == 2):
        return True
    else:
        for i in range(2,a):
            if(a % i == 0):
                return False
        return True


while True:
    sayi = input("Sayı : ")

    if(sayi == "q"):
        break
    else:
        sayi = int(sayi)

        if(asalMi(sayi)):
            print(sayi, "asal bir sayıdır")
        else:
            print(sayi, "asal bir sayı değildir")